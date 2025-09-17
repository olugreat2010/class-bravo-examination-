def validate_pin(pin):
    if pin == '1234':
        return True
    else:
        return False
    
def withdrawal(amount):
    if amount <= "5000":
        return True
    else:
        return False
    
def length_account(receipent_account):
    for char in receipent_account:
        if len (receipent_account) == 10:
            return True
    return False    

def transfer_amount(amount):
    if amount <= "5000":
        return True
    else:
        print("insufficient fund")
        
    
def deposit_amount(amount):
   # balance = "5000"
    if amount >= "100":
        #print(f"new balance{balance + amount}.")
        return True
    else:
        return False
        #print("invalid operation,try again.")
    
def deposit(pin,amount):
    if validate_pin(pin) == True and deposit_amount(amount) == True:
        return True
    else:
        return False