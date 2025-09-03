import time
def is_valid_email(email):
    if '@'  and '.' in email:
        return True
    else:
        return False

def is_password_valid(password):
    if "uppercase"(password) == True and "lowercase"(password) == True and "number"(password) == True and "length"(password) == True and "specialchar"(password) == True:
        return True
    else:
        return False

def register_user():
    print("registration successful")

def south_west():
    print("Ekiti,\n ikeja,\n Abeokuta,\n Akure, \n Oshogbo,\n Ibadan")

#def options():


def atm_pin(ATM_PIN ="2010"):
    return ATM_PIN == "admin"

def attempt(attempt = 3):
    while attempt < 3:
        attempt += 1
    if attempt ==3:
        return False
    else:
        return True      

            
#cont = input("do you want to perform other opptions(yes/no):")
#if cont.lower() != "yes":
    #"break"


def penalty(goalkeeper,kicker):
    if goalkeeper == "LEFT" and kicker == "RIGHT":
        print("goal")
        return True
    else:
        return False

def penalty_2(goalkeeper,kicker):
    if goalkeeper == "RIGHT" and kicker == "LEFT":
        print("goal")
        return True
    else:
        return False

def penalty_3(goalkeeper,kicker):
    if goalkeeper == "RIGHT" and kicker == "RIGHT":
        print("you missed")
        return False
    else:
        return True

def penalty_4(goalkeeper,kicker):
    if goalkeeper == "LEFT" and kicker == "LEFT":
        print("you missed")
        return False
    else:
        return True
           