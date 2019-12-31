import matplotlib.pylab as plt

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