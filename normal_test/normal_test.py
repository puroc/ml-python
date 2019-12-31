import numpy as np
import pandas as pd
from scipy.stats import normaltest
from pylab import plt,rcParams

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 生成正太分布的随机数据
ts2_2 = np.random.randn(100)
result = normaltest(ts2_2, axis=None)
print(result)
ts2_2 = pd.Series(ts2_2)

# 绘制数据分布图
ts2_2.hist(bins=30,alpha = 0.5)
ts2_2.plot(kind = 'kde', secondary_y=True)
plt.title("二阶差分数据分布")
plt.show()