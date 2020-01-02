import numpy as np
import pandas as pd
from scipy.stats import normaltest
from pylab import plt,rcParams

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# 生成正太分布的随机数据
# ts2_2 = pd.Series([1,2,3,4,5,6,7,8,9,10])
ts2_2 = pd.Series([10,9,8,7,6,5,4,3,2,1])
ts2_2 = ts2_2.diff().dropna()