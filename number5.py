import exam_function
print("PENALTY KICK")
goalkeeper=input("enter goal keepers dive direction: ")
kicker=input("enter shooters kick direction: ")
if exam_function.penalty(goalkeeper,kicker)==True:
    print("goal")
else:
    print("you missed")
if exam_function.penalty_2(goalkeeper,kicker)==True:
    print("goal")
else:
    print("you missed")
if exam_function.penalty_3(goalkeeper,kicker)==True:
    print("saved")
else:
    print("goal")
if exam_function.penalty_4(goalkeeper,kicker)==True:
    print("saved")
else:
    print("goal")



