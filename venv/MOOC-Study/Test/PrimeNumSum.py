#coding=utf-8

s=[]
Sum1 = 0
Sum2 = 0
for  x in range(1, 101):
  Sum2 += x

for i in range(1,101):
  for k in range(1, i+1):
    if i%k == 0 and k not in [1, i]:
      s.append(i)
      break

for i in s:
  Sum1 += i
print(Sum2-Sum1-1)


#coding=utf-8
#方法2
'''ls = [];
for i in range(100):
  if i < 2:
    continue

  for j in range(2, i):
    if i % j == 0:
      break
  else:
    ls.append(i)

s = 0
for k in ls:
  s += k
print(s)
