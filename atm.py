import atm_function
print("1 check balance")
print("2 withdraw cash")
print("3 transfer")
print("4 deposit")
print("choose an option")
balance=5000
option=int(input())
if option ==1:
    print("check balance")
    pin=input("enter pin: ")
    if atm_function.validate_pin(pin)==True:
        print(5000)
    else:
        print("incorrect pin")

elif option ==2:
    print("withdraw cash")
    balance=5000
    amount=(input("enter withdrawal amount: "))
    pin=(input("enter your pin: "))
    if atm_function.withdrawal(amount) == True and atm_function.validate_pin(pin) == True:
        print("withdraw succesful")
    else:
        print("insufficient fund")
    
elif option ==3:
    print("transfer")
    balance = 5000
    receipent_account=(input("enter receipent account: "))
    amount=(input("enter transfer amount: "))
    pin=input("enter pin: ")
    if atm_function.length_account(receipent_account)==True and atm_function.validate_pin(pin)==True and atm_function.transfer_amount(amount)==True:
        print("transfer successful")
    else:
        print("operation failed")

elif option == 4:
    print("deposit money")
    balance == "5000"
    amount =(input("enter amount to be deposited: "))
    pin =input("enter your pin: ")
    if atm_function.deposit(pin,amount) == True:
        print("sucessfully deposited")
        print(f"new balance: {"5000" + amount}.")
    else:
        print("invalid operation,try again")
        
    