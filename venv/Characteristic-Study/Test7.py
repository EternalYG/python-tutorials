#coding=utf-8
#限制枚举类的使用说明
#为使枚举类常量成员只能用整数类型，使用enum.IntEnum作为枚举父类
#为防止常量成员值重复，可以为枚举类加上@enum.unique装饰器

import enum

@enum.unique
class WeekDays (enum.IntEnum) :
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5

day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)

if day == WeekDays.MONDAY :
    print("work")
elif day == WeekDays.FRIDAY :
    print("study")