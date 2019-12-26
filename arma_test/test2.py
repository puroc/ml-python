from arma_test.utils import *
import statsmodels as sm

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 导入原始数据
ts = import_ts('/Users/puroc/Desktop/arma/659.csv', 'ts', 'total')
draw_ts(ts,'原始数据')

#对原始数据进行平稳性检验
adf1 = testStationarity(ts)

# 一阶差分
diff = ts.diff(1).dropna()
draw_ts(diff,'一阶差分数据')

#对一阶差分后的数据进行平稳性检验
adf2 = testStationarity(diff)

#通过传入限定的最大值，得到最佳的p值和q值（耗时较长）
import statsmodels.tsa.stattools as st
ic = st.arma_order_select_ic(diff,max_ar=2,max_ma=2,ic=['aic', 'bic', 'hqic'])

#得到最佳p值和q值
# order=ic.aic_min_order
order = (2, 2)

#ARMA模型建模和训练
ARMAmodel = st.ARMA(diff, order).fit()

#得到模型评分
delta = ARMAmodel.fittedvalues - diff.iloc[:0]
score = 1 - delta.var() / diff.var()

draw_two_data(diff,ARMAmodel.fittedvalues,"模型曲线和一阶差分曲线")

import pandas as pd
#输入起始时间和结束时间，进行数据预测（差分后的值，需要进行还原）
# p = ARMAmodel.predict()
result = ARMAmodel.forecast(steps=1)
# p = ARMAmodel.predict(start=pd.to_datetime('2019-07-08 13:45:00'), end=pd.to_datetime('2020-01-01 00:00:00'))

# 一阶差分还原
# result = p.shift(1)
#
# result = revert(p,15.183115)

draw_two_data(ts,result,"原始数据和预测结果")