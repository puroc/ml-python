from utils.file_utils import load_csv
from utils.pic_utils import draw_ts, draw_two_data
from utils.arma_utils import plt, rcParams

plt.rcParams['font.sans-serif'] = ['SimHei']
rcParams['figure.figsize'] = 10, 5

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_202001.csv', 'ts', 'forward_flow_before')
#
# ts2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_202001.csv', 'ts', 'forward_flow_after')
#
# draw_ts(ts1,'before')
#
# draw_ts(ts2,'after')
#
# draw_two_data(ts1,ts2,'对比')

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004012A17/1100HD72004012A17_201911.csv', 'ts', 'forward_flow_before')
#
# ts2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004012A17/1100HD72004012A17_201911.csv', 'ts', 'forward_flow_after')
#
# draw_ts(ts1,'before')
#
# draw_ts(ts2,'after')
#
# draw_two_data(ts1,ts2,'对比')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000003100000001/11000003100000001_201911.csv', 'ts', 'forward_flow_before')
#
# ts2 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000003100000001/11000003100000001_201911.csv', 'ts', 'forward_flow_after')
#
# draw_ts(ts1,'before')
#
# draw_ts(ts2,'after')
#
# draw_two_data(ts1,ts2,'对比')


ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000103100000001/11000103100000001_2019-12-12.csv', 'ts', 'forwardflow')
draw_ts(ts1,'浙江和达流量计2019年11月11日')

ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000103100000001/11000103100000001_2019-12-13.csv', 'ts', 'forwardflow')
draw_ts(ts1,'浙江和达流量计2019年11月12日')

ts3 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000103100000001/11000103100000001_2019-12-14.csv', 'ts', 'forwardflow')
draw_ts(ts3,'浙江和达流量计2019年11月13日')

ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000103100000001/11000103100000001_2019-12-15.csv', 'ts', 'forwardflow')
draw_ts(ts1,'浙江和达流量计2019年11月14日')

ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000103100000001/11000103100000001_2019-12-16.csv', 'ts', 'forwardflow')
draw_ts(ts1,'浙江和达流量计2019年11月15日')

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000023100000002/11000023100000002_2019-12-12.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000023100000002/11000023100000002_2019-12-13.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月12日')
#
# ts3 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000023100000002/11000023100000002_2019-12-14.csv', 'ts', 'forwardflow')
# draw_ts(ts3,'浙江和达流量计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000023100000002/11000023100000002_2019-12-15.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000023100000002/11000023100000002_2019-12-16.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月15日')

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_20191111.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_20191112.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月12日')
#
# ts3 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_20191113.csv', 'ts', 'forwardflow')
# draw_ts(ts3,'浙江和达流量计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_20191114.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/1100HD72004014A13/1100HD72004014A13_20191115.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月15日')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20191111.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20191112.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20191113.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20191114.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20191115.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2019年11月15日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达流量计/11000027100000001/11000027100000001_20190601_20190831.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'浙江和达流量计2018年6月1日到2018年8月31日')


# ts1 = load_csv(
#     '/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20190601_20190831.csv',
#     'ts', 'forwardflow')
# draw_ts(ts1, '青岛积成流量计2018年6月1日到2018年8月31日')
#
# ts1_diff = ts1.diff(1).dropna()
# # ts1_diff = ts1_diff.drop(ts1_diff.idxmax())
#
# draw_ts(ts1_diff, 'xx')

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20191111.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20191112.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20191113.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20191114.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19041/19041_20191115.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月15日')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19071/19071_20191111.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19071/19071_20191112.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19071/19071_20191113.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19071/19071_20191114.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/青岛积成流量计/19071/19071_20191115.csv', 'ts', 'forwardflow')
# draw_ts(ts1,'青岛积成流量计2019年11月15日')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040120A1/1100HD720040120A1_20191111.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040120A1/1100HD720040120A1_20191112.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040120A1/1100HD720040120A1_20191113.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040120A1/1100HD720040120A1_20191114.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040120A1/1100HD720040120A1_20191115.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月15日')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040140A1/1100HD720040140A1_20191111.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040140A1/1100HD720040140A1_20191112.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040140A1/1100HD720040140A1_20191113.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040140A1/1100HD720040140A1_20191114.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/浙江和达压力计/1100HD720040140A1/1100HD720040140A1_20191115.csv', 'ts', 'pressure')
# draw_ts(ts1,'浙江和达压力计2019年11月15日')


# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/新天电信协议水表/29000000002030/29000000002030_20191111.csv', 'ts', 'reading')
# draw_ts(ts1,'新天电信协议水表2019年11月11日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/新天电信协议水表/29000000002030/29000000002030_20191112.csv', 'ts', 'reading')
# draw_ts(ts1,'新天电信协议水表2019年11月12日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/新天电信协议水表/29000000002030/29000000002030_20191113.csv', 'ts', 'reading')
# draw_ts(ts1,'新天电信协议水表2019年11月13日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/新天电信协议水表/29000000002030/29000000002030_20191114.csv', 'ts', 'reading')
# draw_ts(ts1,'新天电信协议水表2019年11月14日')
#
# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/新天电信协议水表/29000000002030/29000000002030_20191115.csv', 'ts', 'reading')
# draw_ts(ts1,'新天电信协议水表2019年11月15日')

# ts1 = load_csv('/Users/puroc/PycharmProjects/ml-python/av_test/data/东鹏水表/10042000620001029/10042000620001029_all.csv', 'ts', 'reading')
# draw_ts(ts1,'东鹏水表全部数据')
