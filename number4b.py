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