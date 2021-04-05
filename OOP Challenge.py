# OOP practice by creating a simple bank account class
# The bank account has 2 methods, deposit and withdraw

class Account:  # Create the Account class
    def __init__(self, owner, balance=0):  # constructor and arguments for the class
        self.owner = owner  # assignment of the owner variable for the object instance
        self.balance = balance  # assignment of the balance

    def __str__(self):  # special str method to allow for output of the account owner and balance
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, dep):  # deposit method
        if dep > 0:  # Checks if the deposit is greater than 0
            self.balance += dep  # updates balance to add deposit
            print('Deposit Accepted')

        else:  # if deposit is less or equal to 0 will give user this message
            'Enter an Amount Greater than 0'

    def withdraw(self, draw):  # withdrawal method
        if draw < self.balance:  # checks that withdrawal is possible by comparing balance and withdrawal request
            self.balance -= draw  # updates balance
            print('Withdrawal Accepted')

        else:  # if the withdrawal is too high, user will be given the message
            print('Funds Unavailable')


# Tests
acct1 = Account('Xhevair', 100)  # creating instance of Account object

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
print(acct1.balance)

acct1.withdraw(75)
print(acct1.balance)

acct1.withdraw(500)

print(acct1)

acct1. deposit(50)
print(acct1)

