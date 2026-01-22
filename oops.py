class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
# student1 = Student("Alice", 20)
# print(student1)
# print(student1.name)
# student1.display_info()

class BankAccount:
    def __init__(self,account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
    
    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}, Account Number: {self.account_number}, Balance: {self.balance}")