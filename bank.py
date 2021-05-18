class BankAccount:
    pin="ggh2034"
    AccountNumber=5432454

    def __init__(self,balance,fixed):
        self.balance=balance
        self.fixed=fixed

    def save(self):
        return f"I will add 300 in my {self.fixed}"
    def withdraw(self):
        return f"I will withdraw 100 in my {self.balance}"
