import pandas as pd
import pyecharts as pe

dfs = pd.read_excel('600177.xlsx', index_col='交易日期')
dfs = dfs.sort_values(['交易日期'], ascending=True)
'''
# 计算股票真实日涨跌幅
df['前收盘价'] = df['收盘价'].shift()
df['涨跌幅'] = df['收盘价'] / df['前收盘价'] - 1
# 计算涨跌停价格
df['涨停价'] = df['前收盘价'] * 1.1
df['跌停价'] = df['前收盘价'] * 0.9
# 计算股票资金曲线
df['资金曲线'] = (1 + df['涨跌幅']).cumprod()
df.loc[:, '资金曲线'] = df['资金曲线'] / df['资金曲线'].iat[1]
# 计算股票后复权价
df['收盘价_后复权'] = df['资金曲线'] * df['收盘价'].iat[1]
df['开盘价_后复权'] = df['开盘价'] / df['收盘价'] * df['收盘价_后复权']
df['最高价_后复权'] = df['最高价'] / df['收盘价'] * df['收盘价_后复权']
df['最低价_后复权'] = df['最低价'] / df['收盘价'] * df['收盘价_后复权']
# 由于第一行有缺失值，影响后续的计算处理，所以我们把第一行缺失值的删掉
df = df.dropna(how='any')
'''


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


df_ma = ma_mark(dfs, 50, 200)
x = dfs.index.astype('str')
y1 = df_ma['收盘价_后复权'].round(2)  # 保留两位小数
y2 = df_ma['MA50'].round(2)
y3 = df_ma['MA200'].round(2)

lin = pe.Line('双均线策略信号')
lin.add('收盘价_后复权', x, y1)
lin.add('MA50', x, y2)
lin.add('MA200', x, y3, is_datazoom_show=True, datazoom_type='both', tooltip_trigger='axis',
        tooltip_axispointer_type='cross')
lin.render('双均线策略信号.html')
