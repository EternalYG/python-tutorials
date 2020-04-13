#coding=utf-8
#日期时间的格式化输出实例

import datetime as dt

d = dt.datetime.today()
print(d)
print(d.strftime('%Y-%m-%d %H:%M:%S'))

str_date = '2018-02-28 10:40:26'
date = dt.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(date)

