'''current_balance = 500000
default_pin=2010
default_deposit=5000
default_transfer=50000
default_airtime=200
print("1 buy airtime")
print("2 transfer")
print("3 deposit")
print("4 withdraw")
print("5 balance")
print("choose an option")
option=int(input(  ))
if(option==1):
    airtime_amount=int(input("enter airtime amount: "))
    receipent=int(input("enter phone number: "))
    pin=int(input("enter 4 digit pin: "))
    if(airtime_amount>=default_airtime):
        if(pin==default_pin):
            print("recharge successful")
        else:
            print("incorrect pin")
    else:
        print("recharge unsuccessful")
elif(option==2):
    acct_no=int(input("enter receipent account: "))
    if "atm_function".len_acc_no(acct_no) == True:
        print("account name; onine blessing")
        transfer_amount=int(input("enter transfer amount: "))
        pin=int(input("enter 4 digit pin: "))
        if(transfer_amount<=default_transfer):
            if(pin==default_pin):
                print("transfer successful")
                print("thank you for banking with opay")
            else:
                print("incorrect pin")
        else:
            print("insufficient fund")
    else:
        print("invalid account number")
elif (option==3):
    deposit_account=int(input("enter account number: "))
    deposit_amount=int(input("enter deposit amount: "))
    pin=int(input("enter 4 digit pin: "))
    if(deposit_amount>=default_deposit):
        if(pin==default_pin):
            print("transaction successful")
            print("deposit_amount+balance")
        else:
            print("incorrect pin")
    else:
        print("invalid operation")
elif(option==4):
    withdrawal_amount=int(input("enter withdrawal amount: "))
    pin=int(input("enter 4 digit pin: "))
    if(pin==default_pin):
        if(withdrawal_amount< current_balance):
            print("withdrawal successful")
            print(f"current_balance - withdrawal_amount")
        else:
            print("insufficient fund")
    else:
        print("incorrect pin")
elif(option==5):
    print("# 500000 NGN")'''


#this is number 4b
class_B = {}
class_B["student1"] ={}
class_B["student1"]["name"]= "samuel alex"
class_B["student1"]["age"]= "15"
class_B["student1"]["major"]= "Agric"
class_B["student1"]["gender"]= "male"

class_B["student2"] ={}
class_B["student2"]["name"]= "micheal adam"
class_B["student2"]["age"]= "13"
class_B["student2"]["major"]= "bio chem"
class_B["student2"]["gender"]= "male"

class_B["student3"] ={}
class_B["student3"]["name"]= "mary jane"
class_B["student3"]["age"]= "16"
class_B["student3"]["major"]= "zoologist"
class_B["student3"]["gender"]= "male"

class_B["student4"] ={}
class_B["student4"]["name"]= "anabella gold"
class_B["student4"]["age"]= "14"
class_B["student4"]["major"]= "nothing"
class_B["student4"]["gender"]= "female"

#to display student one name
print(class_B["student1"]["name"])
#to display student4 record
print(class_B["student4"])
for student in class_B.values():
    student["phone"] = ""
#to update student one age
class_B["student1"]["age"] = 58
print(class_B)

#to add phone field for all students
class_B["student1"]["phone"] ="N/A"
print(class_B["student1"])
class_B["student2"]["phone"] ="N/A"
print(class_B["student2"])
class_B["student3"]["phone"] ="N/A"
print(class_B["student3"])
class_B["student4"]["phone"] ="N/A"
print(class_B["student4"])

#to upate student two major
class_B["student2"]["major"] = "HTML"
print(class_B)
#to update student 3 gender
class_B["student3"]["gener"] = "female"
print(class_B)
#to remove student2 from the dictionary
class_B.pop("student2")
print(class_B)
#to remove student 4 age
class_B.pop["student4"]["age"]
print(class_B)














