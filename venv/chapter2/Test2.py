#coding=utf-8
#类方法、静态方法实例

class Account:
    interest_rate = 0.0668

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount = amount

    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)

interest1 = Account.interest_by(12000.00)
print('计算利息：{0:.4f}'.format(interest1))
interest2 = Account.interest_with(12000.00)
print('计算利息：{0:.4f}'.format(interest2))