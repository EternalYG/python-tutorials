#coding=utf-8
#try-except语句释放资源

import datetime as dt

def read_date_from_file(filename):
    try:
        file = open(filename)
    except OSError as e:
        print('打开文件失败')
    else:
        print('打开文件成功')
        try:
            in_date = file.read()
            in_date = in_date.strip()
            date = dt.datetime.strptime(in_date, '%Y-%m-%d')
            return date
        except (ValueError,OSError)  as e:
            print('处理异常...')
        finally:
            file.close()

date = read_date_from_file('readme.txt')
print('日期 = {0}'.format(date))