class BankAccount:
    name = ""
    account_num = 0
    balance = 0

    def __init__(self, val1, val2):
        self.name = val1
        self.account_num = val2

    def __repr__(self):
        return self.name + "님의 계좌 " + str(self.account_num) + "의 잔고는 " + str(self.balance) + "원입니다."

    def deposit(self, money):
        self.balance += money
        print(str(money) + "원이 입금되었습니다. 잔고는 " + str(self.balance) + "원입니다.")

    def withdraw(self, money):
        if(self.balance < money):
            print("계좌 잔고는 " + str(self.balance) + "원으로 인출 요구 금액 " + str(money) + "보다 작습니다.")
        else:
            self.balance -= money
    
account1 = BankAccount("홍길동", "1234-0001")
print(account1)
account1.deposit(2000)
print(account1)
account1.withdraw(500)
print(account1)
account1.withdraw(5000)
