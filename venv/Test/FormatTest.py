#coding-utf-8
#立方格式化输出
'''a = eval(input())
print("{:-^20}".format(pow(a, 3)))'''

#coding=utf-8
#平方根格式化输出
'''import math
a = eval(input())
print("{:+>30.3f}".format(pow(a, 0.5)))'''

#coding=utf-8
#星号三角形格式化输出
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
