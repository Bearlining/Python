import pandas as pd
import pyecharts as pe

dfs = pd.read_excel('600177.xlsx', index_col='交易日期')
dfs = dfs.sort_values(['交易日期'], ascending=True)


# 自动生成特定长短周期数据的函数
def ma_mark(dfr, n, m):
    '''
    :param dfr: 原始股票数据
    :param n: 统计短周期
    :param m: 统计长周期
    '''

    assert n < m, '统计短周期n必须小于统计长周期m'
    assert m < dfr.shape[0], '统计长周期m必须小于数据长度'
    # 制作数据备份
    df = dfr.copy()
    # 计算双均线
    df['MA%s' % n] = df['收盘价_后复权'].rolling(n).mean()
    df['MA%s' % m] = df['收盘价_后复权'].rolling(m).mean()
    # 买入信号标记
    df.loc[(df['MA%s' % n] > df['MA%s' % m]) &
           (df['MA%s' % n].shift(1) < df['MA%s' % m].shift(1)), '交易信号'] = 1
    # 卖出信号标记
    df.loc[(df['MA%s' % n] < df['MA%s' % m]) &
           (df['MA%s' % n].shift(1) > df['MA%s' % m].shift(1)), '交易信号'] = 0
    # 涨停无法买入标记
    df.loc[(df['收盘价'] >= df['涨停价']) &
           (df['交易信号'] == 1),
           '交易信号'] = None
    # 跌停无法卖出标记
    df.loc[(df['收盘价'] <= df['跌停价']) &
           (df['交易信号'] == 0),
           '交易信号'] = None
    # 持仓状态标记
    df['持仓状态'] = df['交易信号'].fillna(method='ffill').shift().fillna(0)
    # 返回数据
    return df

'''
df_ma = ma_mark(dfs, 50, 200)
# 1.持仓分组标记
# 新建持仓分组列，直接赋值为index——交易日期
df_ma['持仓分组'] = df_ma.index

# 由于持仓状态应该是买之前的状态都一样，买了之后卖出之前也应该是一样的，所以设置一下
# 先将持仓状态上一个等于下一个的持仓分组设成空值，再用向前填充的方法将持仓分组都
# 成最开始产生该状态的日期

df_ma.loc[df_ma['持仓状态'] == df_ma['持仓状态'].shift(), '持仓分组'] = None
df_ma['持仓分组'].fillna(method='ffill', inplace=True)

# 2.策略涨跌幅及手续费计算
# 预计算策略涨跌幅，当持仓为0，策略涨跌幅也是0；持仓为1，策略涨跌幅=股票涨跌幅
df_ma['涨跌幅_策略'] = df_ma['涨跌幅'] * df_ma['持仓状态']
df_ma.loc[(df_ma['持仓状态'] != 0) &
          (df_ma['持仓状态'] != df_ma['持仓状态'].shift()),
            '涨跌幅_策略'] = (1 + df_ma['涨跌幅_策略']) * (1 - 0.0008) - 1
# 找到开仓组的最后一行（最后一行持仓状态为1，下一行为0），扣除手续费
df_ma.loc[(df_ma['持仓状态'] != 0) &
          (df_ma['持仓状态'] != df_ma['持仓状态'].shift(-1)),
            '涨跌幅_策略'] = (1 + df_ma['涨跌幅_策略']) * (1 - 0.0008) -1

# 计算并更新策略资金曲线
df_ma.loc[:, '资金曲线_策略'] = (1 + df_ma['涨跌幅_策略']).cumprod()
df_ma.loc[:, '资金曲线_策略'] = df_ma['资金曲线_策略'] / df_ma['资金曲线_策略'].iat[0]

# 计算最大回撤（策略在每个交易日，相对之前最高点跌幅是多大）
df_ma['最大回撤'] = df_ma['资金曲线_策略'].cummax()  # 返回序列中累计的最大值，[3,3,6,2]为[3,3,6,6]
df_ma.loc[:, '最大回撤'] = 1 - df_ma['资金曲线_策略'] / df_ma['最大回撤']

dic = {'股票资金曲线终值':df_ma['资金曲线'].iat[-1],
       '策略资金曲线终值':df_ma['资金曲线_策略'].iat[-1],
       '相对收益':df_ma['资金曲线_策略'].iat[-1]/df_ma['资金曲线'].iat[-1],
       '总交易次数':df_ma['持仓分组'].unique().shape[0],
       '平均持仓时间':(df_ma.index[-1] - df_ma.index[0])/df_ma['持仓分组'].unique().shape[0],
       '历史最大回撤':df_ma['最大回撤'].max(),
       '股票夏普率':df_ma['涨跌幅'].mean()/df_ma['涨跌幅'].std(ddof=0),
       '策略夏普率':df_ma['涨跌幅_策略'].mean()/df_ma['涨跌幅_策略'].std(ddof=0)}
# 以上是迄今为止做的操作，下面开始搞函数
'''

def fund_curve(dfr, tr=.0008):
    '''
    【回测：资金曲线及绩效指标计算】
    :param dfr: 标记交易信号及持仓状态后的股票数据
    :param tr: 单次交易综合手续费，默认万分之8
    :return:
    '''
    # 拷贝一份数据
    df = dfr.copy()
    # 标记多空持仓组别
    df['持仓分组'] = df.index
    df.loc[df['持仓状态'] == df['持仓状态'].shift(), '持仓分组'] = None
    df['持仓分组'].fillna(method='ffill', inplace=True)
    # 计算策略基本涨跌幅，持仓为0则当日策略基本收益率也为0
    df['涨跌幅_策略'] = df['涨跌幅'] * df['持仓状态']
    # 筛选所有非空持仓并扣除开平仓手续费
    df.loc[(df['持仓状态'] != 0) &
              (df['持仓状态'] != df['持仓状态'].shift()),
              '涨跌幅_策略'] = (1 + df['涨跌幅_策略']) * (1 - tr) - 1

    df.loc[(df['持仓状态'] != 0) &
              (df['持仓状态'] != df['持仓状态'].shift(-1)),
              '涨跌幅_策略'] = (1 + df['涨跌幅_策略']) * (1 - tr) - 1
    # 计算并更新策略资金曲线
    df.loc[:, '资金曲线_策略'] = (1 + df['涨跌幅_策略']).cumprod()
    df.loc[:, '资金曲线_策略'] = df['资金曲线_策略'] / df['资金曲线_策略'].iat[0]

    # 计算最大回撤
    df['最大回撤'] = df['资金曲线_策略'].cummax()  # 返回序列中累计的最大值，[3,3,6,2]为[3,3,6,6]
    df.loc[:, '最大回撤'] = 1 - df['资金曲线_策略'] / df['最大回撤']

    return df,{'股票资金曲线终值':df['资金曲线'].iat[-1],
               '策略资金曲线终值':df['资金曲线_策略'].iat[-1],
               '相对收益':df['资金曲线_策略'].iat[-1]/df['资金曲线'].iat[-1],
               '总交易次数':df['持仓分组'].unique().shape[0],
               '平均持仓时间':(df.index[-1] - df.index[0])/df['持仓分组'].unique().shape[0],
               '历史最大回撤':df['最大回撤'].max(),
               '股票夏普率':df['涨跌幅'].mean()/df['涨跌幅'].std(ddof=0),
               '策略夏普率':df['涨跌幅_策略'].mean()/df['涨跌幅_策略'].std(ddof=0)}


df_ma = ma_mark(dfs, 10, 20)
result = fund_curve(df_ma)

ling = pe.Line('资金曲线')
x = df_ma.index.astype('str')
y1 = result[0]['资金曲线']
y2 = result[0]['资金曲线_策略']
ling.add('资金曲线', x, y1, is_datazoom_show=True)
ling.add('资金曲线_策略', x, y2)
ling.render('资金曲线比较2.html')
# 用更短的周期明显策略资金曲线更接近股票原本的资金曲线了
