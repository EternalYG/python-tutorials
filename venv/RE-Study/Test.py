#coding=utf-8
#正则表达式实例

import  re

p1 = r'\w+@qq\.com'
p2 = r'^\w+@qq\.com$'

text = "Yang's email is yang_123@qq.com."
m1 = re.search(p1, text)
print(m1)

m2 = re.search(p2, text)
print(m2)

email =  'yang_123@qq.com'
m3 = re.search(p2, email)
print(m3)

