
class BankAccount:
    account = []

    def __init__(self, balance,intRate):
        self.balance = balance
        self.intRate = intRate
        BankAccount.account.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.intRate)
        return self

    def yield_interest(self):
        print(self.intRate)
        return self


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(intRate=0.05, balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        return self.account.display_account_info()

guido = User('Guido', 'email') 

guido.make_deposit(500)
guido.display_user_balance()