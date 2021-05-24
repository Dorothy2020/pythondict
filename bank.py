class BankAccount:
    pin="ggh2034"
    AccountNumber=5432454

    def __init__(self,balance,phone_number, name):
        
        self.phone_number=phone_number
        self.name=name
        self.balance=0
    def save(self):
        return f"I will add 300 in my {self.fixed}"
    def withdraw(self):
        return f"I will withdraw 100 in my {self.balance}"
    def show_balance(self):
        return f"Hello,{self.name} your balance is {self.balance}"
    def deposit(self,amount):
      if amount>self.balance:
        self.balance+=amount
        return f"show {self.show_balance()}"
    def withdraw(self,amount):
        self.balance-=amount
        if amount> self.balance:
         return f"Your balance is {self.balance} you cannot withdraw {amount}"
        else:
            return self.show_balance

    def borrow(self,amount):
       return f"Hello {self.name} you are borrowed {amount} "
    
    def repay(self,amount):
        return f"Hello {self.name} I have repaid {amount} "
        
    


