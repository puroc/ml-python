import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from pylab import *


TIME_FORMAT = "%Y/%m/%d %H:%M:%S"

# 导入csv数据
def import_ts(path,index_col,ts_col):
    data = pd.read_csv(path, index_col=index_col)
    # data = pd.read_csv('/Users/puroc/Desktop/arma/659.csv', index_col='ts')
    ts = data[ts_col]
    ts.index = pd.to_datetime(ts.index)
    return ts

# 移动平均图
def draw_trend(timeSeries, size):
    f = plt.figure(facecolor='white')
    # 对size个数据进行移动平均
    rol_mean = timeSeries.rolling(window=size).mean()
    # 对size个数据进行加权移动平均
    rol_weighted_mean = pd.DataFrame.ewm(timeSeries, span=60).mean()
    # rol_weighted_mean = pd.ewma(timeSeries, span=size)

    timeSeries.plot(color='blue', label='Original')
    rol_mean.plot(color='red', label='Rolling Mean')
    rol_weighted_mean.plot(color='black', label='Weighted Rolling Mean')
    plt.legend(loc='best')
    plt.title('Rolling Mean')
    plt.show()

# 画图
def draw_ts(timeSeries,title):
    f = plt.figure(facecolor='white')
    plt.plot(timeSeries,color='blue')
    plt.title(title)
    plt.show()

def draw_two_data(data1,data2,title):
    f = plt.figure(facecolor='white')
    plt.plot(data1,color='blue')
    plt.plot(data2,color='red')
    plt.title(title)
    plt.show()

# 单位根ADF检验
def testStationarity(timeSeries):
    dftest = adfuller(timeSeries)
    # 对上述函数求得的值进行语义描述
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    return dfoutput

# 自相关和偏相关图，默认阶数为31阶
def draw_acf_pacf(ts, lags=31):
    f = plt.figure(facecolor='white')
    ax1 = f.add_subplot(211)
    plot_acf(ts, lags=31, ax=ax1)
    ax2 = f.add_subplot(212)
    plot_pacf(ts, lags=31, ax=ax2)
    plt.show()

#将差分值进行还原
def revert(diffValues, *lastValue):
    for i in range(len(lastValue)):
        result = []
        lv = lastValue[i]
        for dv in diffValues:
            lv = dv + lv
            result.append(lv)
        diffValues = result
    return diffValues

def add_min(current_time,min):
    return (datetime.datetime.strptime(current_time, TIME_FORMAT) + datetime.timedelta(minutes=min)).strftime(TIME_FORMAT)