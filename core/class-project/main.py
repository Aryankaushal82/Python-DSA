import json
import random
import string
from pathlib import Path

class Bank:
    data = []
    database ="data.json"

    try:
        if Path(database).exists():
            with open(database, "r") as fs:
                data = json.loads(fs.read()) 
        else:
            print("database not found")
    except Exception as err:
        print("error: ", err)

    @staticmethod  # static method is used to call the method without creating an instance of the class
    def __update(info):
        try:
            with open(Bank.database, "w") as fs:
                fs.write(json.dumps(Bank.data))
        except Exception as err:
            print("error: ", err)
        else:
            print("Success")
            
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*-+",k=3)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
        


    def createAccount(self):
        info = {
            "name": input("enter your name: "),
            "age": int(input("enter your age: ")),
            "email": input("enter your email: "),
            "pin": input("enter your 4 number pin: "),
            "accountNo.":Bank.__accountgenerate(),
            "balance": 0
        }
        if info["age"] < 18:
            print("you are not eligible to create an account")
        elif len(str(info["pin"])) != 4:
            print("pin must be 4 digits")
        else:
            print("Your Request is being processed...")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please note down your account number for future reference")
            Bank.data.append(info)
            Bank.__update(info)
    
    
    def depositeMoney(self):
        accNum = input("enter your account number: ")
        pin = input("enter your pin: ")
        userData = [i for i in Bank.data if i["accountNo."] == accNum and i["pin"] == pin]
        if not userData:
            print("Account not found")
        else:
            print("Your Current Balance is: ", userData[0]["balance"])
            amount = int(input("enter the amount you want to deposite: "))
            if amount <= 0:
                print("amount must be greater than 0")
            else:
                userData[0]["balance"] += amount
                Bank.__update(userData[0])
                print("deposite successful")
    
    def withdrawMoney(self):
        accNum = input("enter your account number: ")
        pin = input("enter your pin: ")
        userData = [i for i in Bank.data if i["accountNo."] == accNum and i["pin"] == pin]
        if not userData:
            print("Account not found")
        else:
            print("Your Current Balance is: ", userData[0]["balance"])
            amount = int(input("enter the amount you want to withdraw: "))
            if amount <=0:
                print("amount must be greater than 0")
            elif amount > userData[0]["balance"]:
                print("insufficient balance")
            else:
                userData[0]["balance"] -= amount
                Bank.__update(userData[0])
                print("withdraw successful")
                
    def showDetails(self):
        accNum = input("enter your account number: ")
        pin = input("enter your pin: ")
        userData = [i for i in Bank.data if i["accountNo."] == accNum and i["pin"] == pin]
        if not userData:
            print("Account not found")
        else:
            for i in userData[0]:
                print(f"{i}: {userData[0][i]}")
    
    def updateDetails(self):
        print("press 1 to update name")
        print("press 2 to update email")
        print("press 3 to update pin")
        resp = int(input("tell your response: "))
        accNum = input("enter your account number: ")
        pin = input("enter your pin: ")
        userData = [i for i in Bank.data if i["accountNo."] == accNum and i["pin"] == pin]
        if not userData:
            print("Account not found")
        else:
            if resp ==1:
                userData[0]["name"] = input("enter your new name: ")
            elif resp == 2:
                userData[0]["email"] = input("enter your new email: ")
            elif resp == 3:
                newPin = input("enter your new pin: ")
                if len(str(newPin)) != 4:
                    print("pin must be 4 digits")
                else:
                    userData[0]["pin"] = newPin
            else:
                print("invalid response")
            print("do you want to update more details? (y/n)")
            check = input("tell your response: ")
            if check.lower() == "y":
                Bank.__update(userData[0])
                print("update successful")
    
    def deleteAccount(self):
        accNum = input("enter your account number: ")
        pin = input("enter your pin: ")
        userData = [i for i in Bank.data if i["accountNo."] == accNum and i["pin"] == pin]
        if not userData:
            print("Account not found")
        else:
            print("Do you really want to delete your account? (y/n)")
            check = input("tell your response: ")
            if check.lower() == "y":
                Bank.data.remove(userData[0])
                Bank.__update(userData[0])
                print("account deleted successfully")
            else: pass
            
            


user = Bank()

 

print("press 1 for creating an account")
print("press 2 for deposite monye to your account")
print("press 3 for withdraw money from your account")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting the account")
print("press 7 for exit")


check = int(input("tell your response: "))

if check ==1:
    user.createAccount()
    
if check == 2:
    user.depositeMoney()

if check == 3:
    user.withdrawMoney()

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()
if check == 6:
    user.deleteAccount()

if check == 7:
    print("thank you for using our services")

