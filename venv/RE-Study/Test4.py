#coding=utf-8
#正则表达式量词的使用

import re

m = re.search(r'\d?', '87654321')
print(m)

m = re.search(r'\d?', 'ABC')
print(m)

m = re.search(r'\d*', '87654321')
print(m)

m = re.search(r'\d*', 'ABC')
print(m)

m = re.search(r'\d+', '87654321')
print(m)

m = re.search(r'\d+', 'ABC')
print(m)

m = re.search(r'\d{8}', '87654321')
print(m)

m = re.search(r'\d{8}', 'ABC')
print(m)

m = re.search(r'\d{7,8}', '87654321')
print(m)

m = re.search(r'\d{9,}', '87654321')
print(m)