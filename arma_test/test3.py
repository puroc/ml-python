import pandas as pd
import datetime,time

# df = pd.DataFrame(columns=["ts","value"])
#
# for i in range(5):
#     df = df.append({"ts": "2019-01-01 10:00:00","value":i}, ignore_index=True)

start_day = datetime.datetime.strptime("2019-7-8 14:30:00", '%Y-%m-%d %H:%M:%S')

print((start_day+datetime.timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S"))