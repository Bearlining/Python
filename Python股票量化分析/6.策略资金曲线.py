import pandas as pd
import pyecharts as pe

df = pd.read_excel('持仓分组标记.xlsx', index_col='交易日期')
df = df.sort_values(['交易日期'], ascending=True)


# 计算并更新策略资金曲线
df.loc[:, '资金曲线_策略'] = (1 + df['涨跌幅_策略']).cumprod()
df.loc[:, '资金曲线_策略'] = df['资金曲线_策略'] / df['资金曲线_策略'].iat[0]

# 计算最大回撤（策略在每个交易日，相对之前最高点跌幅是多大）
df['最大回撤'] = df['资金曲线_策略'].cummax()  # 返回序列中累计的最大值，[3,3,6,2]为[3,3,6,6]
df.loc[:, '最大回撤'] = 1 - df['资金曲线_策略'] / df['最大回撤']

# 新建一个字典来存储各绩效指标
# 股票资金曲线终值：即股票资金曲线在最近一个交易日的数值，展示了开盘以来累计涨跌的收益情况
# 策略资金曲线终值：即策略资金曲线在最近一个交易日的数值，展示了开盘以来累计涨跌的收益情况
# 相对收益：最近一个交易日，策略资金曲线与股票型资金曲线的比值
# 总交易次数：所有的买入卖出次数总计
# 平均持仓时间：持仓一次平均的时间长度
# 历史最大回撤：策略历史上，从最高点到最低点的跌幅
# 股票夏普率：股票平均涨跌幅/涨跌幅的波动，这里简化计算，假设无风险收益率为0
# 策略夏普率：策略平均涨跌幅/涨跌幅的波动
dic = {'股票资金曲线终值':df['资金曲线'].iat[-1],
       '策略资金曲线终值':df['资金曲线_策略'].iat[-1],
       '相对收益':df['资金曲线_策略'].iat[-1]/df['资金曲线'].iat[-1],
       '总交易次数':df['持仓分组'].unique().shape[0],
       '平均持仓时间':(df.index[-1] - df.index[0])/df['持仓分组'].unique().shape[0],
       '历史最大回撤':df['最大回撤'].max(),
       '股票夏普率':df['涨跌幅'].mean()/df['涨跌幅'].std(ddof=0),
       '策略夏普率':df['涨跌幅_策略'].mean()/df['涨跌幅_策略'].std(ddof=0)}

ling = pe.Line('资金曲线')
x = df.index.astype('str')
y1 = df['资金曲线']
y2 = df['资金曲线_策略']
ling.add('资金曲线', x, y1, is_datazoom_show=True)
ling.add('资金曲线_策略', x, y2)
ling.render('资金曲线比较.html')