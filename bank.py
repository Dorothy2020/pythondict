from datetime import datetime


class BankAccount:
    pin="ggh2034"
    AccountNumber=5432454
    from datetime import datetime


    def __init__(self,phone_number, name):
        self.phone_number=phone_number
        self.name=name
        self.balance=0
        self.statement=[]
        
       
    def save(self):
        return f"I will add 300 in my {self.fixed}"
    def withdraw(self):
        return f"I will withdraw 100 in my {self.balance}"
    def show_balance(self):
        return f"Hello,{self.name} your balance is {self.balance}"
    def deposit(self,amount):
        if amount<=0:
           return "you can nnot deposit"
        else:

          
            self.balance+=amount
            now=datetime.now()
            transaction={"amount":amount,"time":now,"Narration" :"you deposited"}
            self.statement.append(transaction)
        return self.show_balance()

        
    def withdraw(self,amount):
            
    
        if amount> self.balance:
            return f"Your balance is {self.balance} you cannot withdraw {amount}"

        else:
            self.balance-=amount
            now=datetime.now()
            transaction={"amount":"amount","time":now,"Narration" :"you deposited"}
            self.statement.append(transaction)
            return self.show_balance()
            

    # def s(self,amount):
       
    def show_statement(self):
            for transaction in self.statement:
                amount=transaction["amount"]
                narration=transaction["narration"]
                time=transaction["time"]
                date=time.strftime("%d/%m/%y")
                print(f"{date}: {narration} {amount}")
            return 

        # return f"Hello {self.name} you are borrowed {amount} "
    
    def repay(self,amount):
        return f"Hello {self.name} I have repaid {amount} "
    

    
        
    


