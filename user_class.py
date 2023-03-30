class User:		# here's what we have so far
    bank_name=""
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def display_user_balance(self):
        print(f"User: {self.name},Balance:${self.account_balance}")    

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        
guido=User("Guido Martinez","guido@gmail.com")
monty=User("Monty Alvarez","monty@gmail.com")
souheil=User("Souheil Khalfallah","khalfallah.souheil@gmail.com")
User.bank_name = "Bank of Dojo"

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(50)
guido.display_user_balance()
monty.display_user_balance()
souheil.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(100)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
guido.display_user_balance()
monty.display_user_balance()
souheil.display_user_balance()

guido.transfer_money(souheil,50)
guido.display_user_balance()
souheil.display_user_balance()