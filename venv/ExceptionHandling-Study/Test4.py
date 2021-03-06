#coding=utf-8
#with as代码块自动资源管理

import datetime as dt

def read_date_from_file(filename):
    try:
        with open(filename) as file:
            in_date = file.read()

        in_date = in_date.strip()
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except (ValueError, OSError) as e:
        print('处理异常')

date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))