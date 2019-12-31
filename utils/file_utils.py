import pandas as pd

# 导入csv数据
def load_csv(path, index_col, ts_col):
    data = pd.read_csv(path, index_col=index_col)
    ts = data[ts_col]
    ts.index = pd.to_datetime(ts.index)
    return ts