import pandas as pd

from utils.file_utils import load_csv
from utils.pic_utils import draw_ts
from utils.arma_utils import plt, rcParams
import numpy as np
from scipy.stats import kstest,normaltest,anderson

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/20191111.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'2019年11月11日')

ts2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/20191112.csv', 'ts', 'forwardflow')
draw_ts(ts2,'2019年11月12日原始数据')
ts2_1  = ts2.diff().dropna()
draw_ts(ts2_1,'2019年11月12日一阶差分')
ts2_2  = ts2_1.diff().dropna()
draw_ts(ts2_2,'2019年11月12日二阶差分')

ts3 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/20191113.csv', 'ts', 'forwardflow')
# draw_ts(ts3,'2019年11月13日')

ts4 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/20191114.csv', 'ts', 'forwardflow')
# draw_ts(ts4,'2019年11月14日')

ts5 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/20191115.csv', 'ts', 'forwardflow')
# draw_ts(ts5,'2019年11月15日')

ts1 = ts1.append(ts2)
# ts1 = ts1.append(ts3)

# draw_ts(ts1,'2019年11月11日和2019年11月12日和2019年11月13日')
# draw_ts(ts1,'2019年11月11日和2019年11月12日')


# 绘制数据分布图
# ts2.hist(bins = 100,alpha = 0.3,color = 'k',normed = True)
# ts2.plot(kind = 'kde',style = 'k--')
# plt.show()

ts2.hist(bins=30,alpha = 0.5)
ts2.plot(kind = 'kde', secondary_y=True)
plt.title("原始数据分布")
plt.show()

ts2_1.hist(bins=30,alpha = 0.5)
ts2_1.plot(kind = 'kde', secondary_y=True)
plt.title("一阶差分数据分布")
plt.show()

ts2_2.hist(bins=30,alpha = 0.5)
ts2_2.plot(kind = 'kde', secondary_y=True)
plt.title("二阶差分数据分布")
plt.show()



# kstest方法中的参数分别是：待检验的数据，检验方法（这里设置成norm正态分布），均值与标准差
# 返回两个值：statistic → D值，pvalue → P值
# 当p值大于0.05，说明待检验的数据符合为正态分布


# ts2_2 = np.linspace(-15, 15, 9)
# ts2_2 = np.random.randn(10, 20)

# result = kstest(ts2_2, 'norm')
result = normaltest(ts2_2, axis=None)
print(ts2_2.describe())

#
# result = anderson(ts2_2)
print(result)



