import numpy as np
import pandas as pd
from scipy.stats import normaltest
from pylab import plt,rcParams

from utils.file_utils import load_csv
from utils.pic_utils import draw_ts

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 生成正太分布的随机数据
# ts2_2 = np.random.randn(100)
ts2_2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/新天电信协议水表/29000000002030/29000000002030_20191111.csv', 'ts', 'reading')
# ts2_2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/青岛积成流量计/19041/19041_20191111.csv', 'ts', 'forwardflow')
draw_ts(ts2_2,"原始")
# ts2_2 = ts2_2.diff(1).dropna()
# draw_ts(ts2_2,"一阶")
# ts2_2 = ts2_2.diff(1).dropna()
# draw_ts(ts2_2,"二阶")
# ts2_2 = ts2_2.diff(1).dropna()
# draw_ts(ts2_2,"三阶")
result = normaltest(ts2_2, axis=None)
print(result)
ts2_2 = pd.Series(ts2_2)

# 绘制数据分布图
ts2_2.hist(bins=30,alpha = 0.5)
ts2_2.plot(kind = 'kde', secondary_y=True)
plt.title("二阶差分数据分布")
plt.show()