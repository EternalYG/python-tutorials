#coding=utf-8
#datetime、date、和time类实例

import datetime as dt

print(dt.datetime.now())
print(dt.datetime.utcnow())
print(dt.date.today())
print(dt.date.fromtimestamp(99999999.999))

d1 = dt.datetime.today()
d2 = dt.datetime.today()
print(d1, d2)
delta1 = dt.timedelta(10)
d1 += delta1
print(d1)
delta2 = dt.timedelta(weeks=5)
d2 -= delta2
print(d2)

