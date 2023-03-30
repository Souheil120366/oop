class BankAccount:
    all_accounts=[]
    def __init__(self, balance):
        self.int_rate = 0.01
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance-=amount
        else:
               print( "Insufficient funds: Charging a $5 fee")
               self.balance-=5
        return self       
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
           self.balance+= self.balance*self.int_rate
            
        return self
    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()
        
    
souheil=BankAccount(100)
youssef=BankAccount(100)
souheil.deposit(100).deposit(100).deposit(50).withdraw(400).yield_interest().display_account_info()
youssef.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
BankAccount.all_balances()