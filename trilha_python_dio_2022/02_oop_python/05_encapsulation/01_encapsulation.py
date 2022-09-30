class Bank_account:
    def __init__(self, agency, balance=0):
        self._balance = balance
        self.agency = agency

    def deposit(self, value):
        # ...
        self._balance += value

    def to_withdraw(self, value):
        # ...
        self._balance -= value

    def show_balance(self):
        # ...
        return self._balance


bank_account = Bank_account("0001", 100)
bank_account.deposit(100)
print(f"Bank Agency: {bank_account.agency}")
print(f"Current Balance: R${bank_account.show_balance()}")


#Python is strongly, dynamically typed.
#By convention a _ is used for private attributes in Python.