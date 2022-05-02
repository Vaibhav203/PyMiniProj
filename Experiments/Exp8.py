'''
# VAIBHAV BHALIYA    68    SEITB-B3
class Employee():
    c = 0
    def __init__(self, eid, dep, nam, sal):
        Employee.c+=1
        self.Employee_id = eid
        self.department = dep
        self.name = nam
        self.salary = sal
    def display(self):
        print("Employee:    ", self.Employee_id)
        print("Department:  ", self.department)
        print("Name:        ", self.name)
        print("Salary:      %.2f" % self.salary)
    def update(self, newsal):
        self.salary = newsal
i = 1
while i > 0:
    print("1. Enter Details")
    print("2. Update Salary")
    print("3. Exit")
    inn = int(input("Your choice: "))
    if inn == 1:
        nam = input("Your Name:        ")
        dep = input("Your Department:  ")
        eid = input("Your Employee id: ")
        sal = float(input("Enter the salary: "))
        obj1 = Employee(eid, dep, nam, sal)
        obj1.display()
        print()
    elif inn == 2:
        newsal = float(input("New salary = "))
        obj1.update(newsal)
        obj1.display()
        print(" ")
    elif inn == 3:
        print("Exited")
        break
    else:
        print("Enter proper choice")
'''

#Vaibhav Bhaliya    68    seitb-b3
class College:
    def student(self):
        print('Class: College, Method: Student')
    def faculty(self):
        print('Class: College, Method: Faculty')
class Student(College):
    def __init__(self):
        print('Class: Student, Method: __init__')
class Faculty(College):
    def __init__(self):
        print('Class: Faculty, Method: __init__')
a = Student()
a.student()
b = Faculty()
b.faculty()