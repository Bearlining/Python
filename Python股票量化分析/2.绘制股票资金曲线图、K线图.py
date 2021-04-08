import pandas as pd
import pyecharts as pe

df = pd.read_excel('600177.xlsx', index_col='交易日期')
df = df.sort_values(['交易日期'], ascending=True)
'''
# 计算股票真实日涨跌幅
df['前收盘价'] = df['收盘价'].shift()
df['涨跌幅'] = df['收盘价'] / df['前收盘价']
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

# 资金曲线折线图绘制
df['资金曲线'].iloc[1::].plot(x='交易日期', y='资金曲线', figsize=(20, 8),
                          color='r', alpha=0.8,
                          grid=True,
                          rot=45,
                          title='兆易创新（603986）资金曲线折线图')
'''


x = df.index.astype('str')
y = df[['开盘价', '收盘价', '最低价', '最高价']].values

kline = pe.Kline('雅戈尔2010.4.28-2020.4.28不复权K线图')
kline.add('日k', x, y,
          is_datazoom_show=True,
          datazoom_type='both',
          datazoom_range=[80,100],
          mark_point=['max', 'min'],
          is_xaxislabel_align=True,
          tooltip_trigger='axis',
          tooltip_axispointer_type='cross')
kline.render('日K.html')