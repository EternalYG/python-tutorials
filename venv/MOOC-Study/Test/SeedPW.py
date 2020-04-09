#coding=utf-8
#以17为随机数种子，以n为长度，输出3个长度为n的密码
import random

def genpwd(length):
    a = 10**(length-1)
    b = 10**length - 1
    return "{}".format(random.randint(a, b))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
