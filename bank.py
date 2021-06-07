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
        self.loan=0
       
    def save(self):
        return f"I will add 300 in my {self.fixed}"
    def withdraw(self):
        return f"I will withdraw 100 in my {self.balance}"
    def show_balance(self):
        return f"Your {self.name} balance is {self.balance}"
    def deposit(self,amount):
        if amount<=0:
           return "you can cannot deposit"
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

    def borrow(self,amount):
            # self.amount=amount
            # self.loan=0
            if amount<0:
                return f"You can borrow  {self.amount} if you qualify for a loan{amount}"
            elif self.loan>0:
                return f"You don't have a loan {self.loan}"
            elif amount<0.1 *self.balance:
                return f"You cannot borrow ksh {amount}"
            
            else:
                loan=amount*1.05
                self.loan=loan
                self.balance+=amount
                return f"You have successfuly borrowed {self.loan}"

    def repay(self,amount):
        # self.amount=amount
        if amount<0:
            return f"You have an extra amount {amount} in the bank"
        
        elif amount<self.loan:
            self.loan-=amount
            now=datetime.now()
            borrow_transaction={"amount":amount,"time":now,"Narration" :"you have borrowed ksh"}
            self.statement.append(borrow_transaction)
            return f" Hello {self.loan} decrease loan with {amount}"

        else :
            diff=amount-self.loan
            self.loan=0
            self.deposit(diff) 
            now=datetime.now()
            repay_transaction={"amount":amount,"time":now,"Narration" :"repaid loan sucessfully ksh"}
            self.statement.append(repay_transaction)
            return f"You have fully repaid your loan"       




    

    
        
    


