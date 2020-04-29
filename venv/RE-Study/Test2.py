#coding=utf-8
#正则表达式定义字符类的使用

import re

p = r'[Jj]ava'

m = re.search(p, 'I Like Java and Python')
print(m)

m = re.search(p, 'I Like JAVA and Python')
print(m)

m = re.search(p, 'I Like java and Python')
print(m)