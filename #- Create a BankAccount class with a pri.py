#- Create a BankAccount class with a private attribute _balance. Add methods deposit() and withdraw(), ensuring balance can't be directly modified.
class BankAccount:
    def __init__(self, _balance = 0):
        self._balance = _balance

    def deposit(balance):
        dep = input("Enter deposit amount: ")
        _balance += dep
    
    def withdraw(balance):
        wit = input("Enter withdrawal amount: ")
        _balance -= wit


balance = int(input("Enter balance: "))
balance = BankAccount()

deposit(balance)
wwithdraw(balance)