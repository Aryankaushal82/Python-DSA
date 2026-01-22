class Student:
    def __init__(self,name,age,place):
        self.person_name=name
        self.person_age=age 
        self.person_place=place
    def is_adult(self):
        if self.person_age>=18:
            return f"{self.person_name} is an adult"
        else:
            return f"{self.person_name} is not an adult"
    def is_urban(self):
        urban=["hyderabad","bangalore","chennai","mumbai","delhi"]
        if self.person_place in urban:
            return f"{self.person_name} is from urban area"
        else:
            return f"{self.person_name} is from rural area"       
himanshu=Student("Himanshu",21,"Bangalore")
armaan=Student("armaan",20,"Hyderabad")
nakka=Student("nakka",11,"jjg")
tattu=Student("tattu",71,"bread")
print(himanshu.is_urban())



# Create a BankAccount class.


# Requirements:


# Constructor should initialize:
# account_holder_name
# account_number
# balance
# Create methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Create an account object and perform deposit and withdrawal operations.

class bankAccount:
    def __init__(self,account_holder_name,account_number,balance):
        self.account_holder_name=account_holder_name
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        bal=self.balance+amount
        print(f"Balance for {self.account_holder_name} post depositing {amount} amount , updated balace is {bal}")
        self.balance=bal
    def withdraw(self,amount):
        bal=self.balance-amount
        print(f"Balance for {self.account_holder_name} post withdrawing {amount} amount , updated balace is {bal}")
        self.balance = bal
    def display(self):
        print("--------------------------------")
        print("Acc Name  | number  |  balance")
        print(f"{self.account_holder_name} || {self.account_number} || {self.balance}")
        print()

# Use a constructor to initialize:
# length
# width
# Create methods:
# area()
# perimeter()
# Create multiple rectangle objects with different dimensions and print their area and perimeter.

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        area=self.length*self.width
        return area
    def perimeter(self):
        perimeter=2*(self.length+self.width)
        return perimeter
rect=Rectangle(10,5)
print("Area:",rect.area())
print("Perimeter:",rect.perimeter())

# Constructor should initialize:
# employee_id
# name
# basic_salary
# Create a method calculate_salary() that adds:
# 20% HRA
# 10% DA
# Display total salary for the employee.
class employee:
    def __init__(self,employee_id,name,basic_salary):
        self.employee_id=employee_id
        self.name=name
        self.basic_salary=basic_salary
    def calaculate_salary(self):
        hra=0.2*self.basic_salary
        da=0.1*self.basic_salary
        total_salary=self.basic_salary+hra+da
        return total_salary
himanshu=employee(101,"Himanshu",50000)
print(himanshu.calaculate_salary()) 