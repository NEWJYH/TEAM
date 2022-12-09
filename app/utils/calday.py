from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta


def getMonthRage(year, month):
    this_month = datetime(year=year, month=month, day=1).date()
    next_month = this_month + relativedelta.relativedelta(months=1)
    first_day = this_month
    last_day = next_month - timedelta(days=1)
    return (first_day.day, last_day.day)

def getSplitYMD(strobj_time):
    year, month, day = list(map(int, strobj_time.split('-')))
    return (year, month, day)