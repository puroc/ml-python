from arma_test.utils import *

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 导入原始数据
ts = import_ts('/Users/puroc/Desktop/arma/659.csv', 'ts', 'total')
draw_ts(ts,'原始数据')
draw_acf_pacf(ts)
adf1 = testStationarity(ts)

ts_log = np.log(ts)
draw_ts(ts_log,'对数转换')

draw_trend(ts_log, 96)


diff_14 = ts_log.diff(14)
diff_14.dropna(inplace=True)
adf2 = testStationarity(diff_14)

# "multiplicative"
from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(ts_log, model="additive",freq=1)
f = plt.figure(facecolor='white')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
ax1 = f.add_subplot(311)
ax1.plot(trend)
ax2 = f.add_subplot(312)
ax2.plot(seasonal)
ax3 = f.add_subplot(313)
ax3.plot(residual)
plt.show()

# 移动平均
rol_mean = ts_log.rolling(window=12).mean()
rol_mean.dropna(inplace=True)

# 一阶差分
ts_diff_1 = rol_mean.diff(1)
ts_diff_1.dropna(inplace=True)
adf3 = testStationarity(ts_diff_1)

# 一阶差分
ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)
testStationarity(ts_diff_2)

draw_acf_pacf(ts_diff_2, lags=1)

# 拟合
from statsmodels.tsa.arima_model import ARMA
model = ARMA(ts_diff_2, order=(1, 1))
result_arma = model.fit( disp=-1, method='css')



#还原
predict_ts = result_arma.predict()
# 一阶差分还原
diff_shift_ts = ts_diff_1.shift(1)
diff_recover_1 = predict_ts.add(diff_shift_ts)
# 再次一阶差分还原
rol_shift_ts = rol_mean.shift(1)
diff_recover = diff_recover_1.add(rol_shift_ts)
# 移动平均还原
rol_sum = ts_log.rolling(window=11).sum()
rol_recover = diff_recover*12 - rol_sum.shift(1)
# 对数还原
log_recover = np.exp(rol_recover)
log_recover.dropna(inplace=True)


ts = ts[log_recover.index]  # 过滤没有预测的记录
plt.figure(facecolor='white')
log_recover.plot(color='blue', label='Predict')
# ts.plot(color='red', label='Original')
plt.legend(loc='best')
plt.title('RMSE: %.4f'% np.sqrt(sum((log_recover-ts)**2)/ts.size))
plt.show()

