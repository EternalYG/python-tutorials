#coding=utf-8
#时间时区实例

from datetime import datetime, timedelta, timezone

utc_dt = datetime(2018, 8, 19, 23, 59, 59, tzinfo= timezone.utc)
print(utc_dt.strftime('%Y-%m-%d %H:%M:%S'))

bj_tz = timezone(offset= timedelta(hours = 8), name = 'Asia/Beijing')
bj_dt = utc_dt.astimezone(bj_tz)
print(bj_dt.strftime('%Y-%m-%d %H:%M:%S %Z'))


