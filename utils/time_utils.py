from datetime import datetime
from datetime import timedelta

TIME_FORMAT = "%Y/%m/%d %H:%M:%S"

def add_min(current_time,min):
    return (datetime.strptime(current_time, TIME_FORMAT) + timedelta(minutes=min)).strftime(TIME_FORMAT)