#coding=utf-8
#类实例

class Account:
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount


account = Account('Tony', 18000000.0)

print('账户名：{0}'.format(account.owner))
print('账户余额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))



