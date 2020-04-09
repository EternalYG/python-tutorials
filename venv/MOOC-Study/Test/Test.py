#coding=utf-8
#计算1-2+3...-966
'''Sum = 0
for i in range(1, 967):
    if i % 2 != 0:
        Sum += i
    elif i %2 == 0:
        Sum += -i
print(Sum)'''

#coding=utf-8
#字符串分段组合
'''s=input()
res=s.split('-')
print(res[0]+"+"+res[-1])'''

#coding=utf-8
#四位水仙花数打印
'''s=[]
for i in range(1,10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        if i**4 + j**4 + k**4 + l**4 == 1000*i + 100*j + 10*k + l:
          s.append(1000*i + 100*j + 10*k + l)
for i in s:
  if i == s[-1]:
    print(i)
  else:
    print("{0:}".format(i))'''


#coding=utf-8
#输出从n开始的五个质数
def prime(m):
    for i in range(2,m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n_ = int(n)
n_ = n_+1 if n_ < n else n_
count = 5

while count > 0:
    if prime(n_):
        if count > 1:
            print(n_, end=",")
        else:
            print(n_, end="")
        count -= 1
    n_ += 1


