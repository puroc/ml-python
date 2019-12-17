from arma_test.utils import *

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

ts = import_ts('/Users/puroc/Desktop/arma/659.csv', 'ts', 'total')
draw_ts(ts)
draw_acf_pacf(ts)
testStationarity(ts)
