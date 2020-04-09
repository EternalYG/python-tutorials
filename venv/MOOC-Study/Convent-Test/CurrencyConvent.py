#coding=utf-8
TempStr = input("")
if TempStr[0:3] == 'RMB':
    USD = (eval(TempStr[3:]))/6.78
    print("USD{:.2f}".format(USD))
elif TempStr[0:3] == 'USD':
    RMB = 6.78*eval(TempStr[3:])
    print("RMB{:.2f}".format(RMB)

#CurStr = input()
#if CurStr[:3] == "RMB":
#     print("USD{:.2f}".format(eval(CurStr[3:]) / 6.78))
#elif CurStr[:3] in ['USD']:
#    print("RMB{:.2f}".format(eval(CurStr[3:]) * 6.78))

