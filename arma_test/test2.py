from arma_test.utils import *
import statsmodels as sm
import statsmodels.tsa.stattools as st
import pandas as pd
import datetime, time

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 导入原始数据
ts = import_ts('/Users/puroc/Desktop/arma/659.csv', 'ts', 'value')
draw_ts(ts, '原始数据')

# 对原始数据进行平稳性检验
adf1 = testStationarity(ts)

# 一阶差分
diff = ts.diff(1).dropna()
draw_ts(diff, '一阶差分数据')

# 对一阶差分后的数据进行平稳性检验
adf2 = testStationarity(diff)

# 通过传入限定的最大值，得到最佳的p值和q值（耗时较长）


ic = st.arma_order_select_ic(diff, max_ar=2, max_ma=2, ic=['aic', 'bic', 'hqic'])

# 得到最佳p值和q值
# order=ic.aic_min_order
order = (2, 2)

# ARMA模型建模和训练
ARMAmodel = st.ARMA(diff, order).fit()

# 得到模型评分
delta = ARMAmodel.fittedvalues - diff.iloc[:0]
score = 1 - delta.var() / diff.var()

draw_two_data(diff, ARMAmodel.fittedvalues, "模型曲线和一阶差分曲线")

forecast_num = 10000

# 输入起始时间和结束时间，进行数据预测（差分后的值，需要进行还原）
p = ARMAmodel.predict()

f = ARMAmodel.forecast(steps=forecast_num)[0]
# p = ARMAmodel.predict(start=pd.to_datetime('2019/2/16 12:30:00'), end=pd.to_datetime('2019/7/8 13:45:00'))

# 一阶差分还原，给原始数据第一个数，还原后的第一个数应该对应的是第二个时间点
result_p = revert(p, 571383.0)
# 一阶差分还原，给原始数据最后一个数，还原后的第一个数应该对应的是预测的第一个时间点
result_f = revert(f, 754749.0)

# 转换
from pandas import Series, DataFrame

# result_f_ts = {
#     "ts": ["2019/7/8 14:00:00", "2019/7/8 14:30:00", "2019/7/8 14:45:00", "2019/7/8 15:00:00", "2019/7/8 15:15:00",
#            "2019/7/8 15:30:00", "2019/7/8 15:45:00", "2019/7/8 16:00:00", "2019/7/8 16:15:00", "2019/7/8 16:30:00"],
#     "value": [result_f[0], result_f[1], result_f[2], result_f[3], result_f[4], result_f[5], result_f[6], result_f[7], result_f[8],
#               result_f[9]]}
# result_f_df = DataFrame(result_f_ts, columns=["ts", "value"])

result_f_df = pd.DataFrame(columns=["ts", "value"])
result_p_df = pd.DataFrame(columns=["ts", "value"])

forecast_start_time = "2019/7/8 14:30:00"
forecast_time = forecast_start_time
for i in range(forecast_num):
    # 加15分钟
    forecast_time = add_min(forecast_time, 15)
    result_f_df = result_f_df.append({"ts": forecast_time, "value": result_f[i]}, ignore_index=True)

result_f_series = pd.Series(result_f_df['value'].values, index=result_f_df['ts'])
result_f_series.index = pd.to_datetime(result_f_series.index)

# 取原始数据的第一个时间点
predict_start_time = "2019/2/16 12:30:00"
predict_time = predict_start_time
primitive_data_len = len(ts)
# 因为predict是根据一阶差分之后的数据进行预测的，所以会比原始数据少一个。如果是二阶差分就会少两个，以此类推
for i in range(primitive_data_len - 1):
    # 基于原始数据的第一个时间点加15分钟，即等于原始数据的第二个时间点，pridict还原后的第一个数据是与第二个时间点对应的
    predict_time = add_min(predict_time, 15)
    result_p_df = result_p_df.append({"ts": predict_time, "value": result_p[i]}, ignore_index=True)

result_p_series = pd.Series(result_p_df['value'].values, index=result_p_df['ts'])
result_p_series.index = pd.to_datetime(result_p_series.index)

result_series = result_p_series.append(result_f_series)

draw_ts(result_series, "预测数据")

draw_two_data(ts, result_series, "原始数据和预测结果")
