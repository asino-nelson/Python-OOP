# Encapsulation

class Bank_account:
    def __init__(self,balance = 0.0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    # Deposit
    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Amount deposited must be greater than 0")
        self._balance += amount
        
    # Withdraw
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Failed! Amount withdrawn must be greater than 0")
        elif amount > self._balance:
            raise ValueError("Failed! You have insuffient funds")
        self._balance -= amount

account = Bank_account()
print(account.balance)
account.deposit(200)
print(account.balance)
account.withdraw(150)
print(account.balance)