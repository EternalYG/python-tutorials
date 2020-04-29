#coding=utf-8
#正则表达式字符类取反与区间、预定义字符类实例

import re

#p = r'[^0123456789]'
p = r'\D'

m = re.search(p, '1000')
print(m)

m = re.search(p, 'Python 3')
print(m)

text = '你们好Hello'
m = re.search(r'\w', text)
print(m)

m = re.search(r'[A-Za-z0-9]', 'A10.3')
print(m)

m = re.search(r'[0-25-7]', 'A3489C')
print(m)