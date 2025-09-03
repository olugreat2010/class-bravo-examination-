import exam_function
email =str(input("enter your email: "))
if exam_function.is_valid_email(email) ==True:
    print("email accepted")
else:
    print("invalid email format")
    
password =(input("input your password: "))
if exam_function.is_password_valid(password)==True:
    print("password accepted")
else:
    print('invalid password')

if exam_function.is_password_valid(password)==True and exam_function.is_valid_email(email)==True:
    print("registration successful")