import pickle
# Vaibhav Bhaliya   68   SEITB-B3
class Student:
    def __init__(self, name, age, dept, roll):
        self.name = name
        self.age = age
        self.dept = dept
        self.roll = roll
    def display(self):
        print('\n Name: ',self.name,'\n Age: ',self.age,'\n Department: ',self.dept,'\n Roll: ',self.roll)
f = open("termi.dat", "wb")
obj1 = Student(" Vaibhav Bhaliya ", 19, " SEITB-3 ",68)
pickle.dump(obj1 , f)
f.close()
fil = open("termi.dat", "rb")
obj = pickle.load(fil)
obj.display()
fil.close()


'''
# post experiment
#Vaibhav Bhaliya   68   SEITB-B3
with open("Vaibhav.txt", "r") as f:
    lines = f.readlines()
print(lines[-2])
print(lines[-1])

f.close()
'''