class BankAccount:
   def __init__(self,owner,balance):
     self.owner=owner
     self.balance=balance
     
   def get_balance(self):
     return self.balance
    
   def deposit(self,amount):
     self.balance=self.balance+amount
         
   def withdraw(self,amount):
       if 0<amount<=self.balance:
         self.balance=self.balance-amount
       else:
         print("Insufficient balance")
         
acc=BankAccount('Suman',1000)

print("Owner",acc.owner)
print("Balance", acc.get_balance())

acc.deposit(500)
print("Balance after Deposit",acc.get_balance())

acc.withdraw(300)
print("Balance after withdraw :",acc.get_balance())