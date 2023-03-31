class User:		
    def __init__(self, name, email,acc):
        self.name = name
        self.email = email
        self.acc_num = acc
        self.account = BankAccount(int_rate=0.02, balance=0, acc_num=acc)
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received    
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name},Account number: {self.acc_num} Balance:${self.account.balance}")    
        return self
        
class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance,acc_num):
        self.int_rate = int_rate
        self.balance = balance
        self.acc_num = acc_num
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
       
souheil1=User("souheil","souheil@gmail.com",200123550) # Souheil First Account
souheil2=User("souheil","souheil@gmail.com",300568960) # Souheil Second Account
youssef1=User("youssef","youssef@gmail.com",140123550) # Youssef First Account
youssef2=User("youssef","youssef@gmail.com",150123660) # Youssef Second Account

souheil1.make_deposit(100).make_withdrawal(50).display_user_balance()
souheil2.make_deposit(200).make_withdrawal(70).display_user_balance()
youssef1.make_deposit(400).make_withdrawal(170).display_user_balance()              
youssef2.make_deposit(500).make_withdrawal(270).display_user_balance()
