'''
#Vaibhav Bhaliya    68    SEITB-B3
class Account:
 def __init__(self):
     self.bal=0
     print('Account created successfully.')
 def dep(self):
     amount=int(input('Enter amount to deposit:'))
     self.bal+=amount
     print('New Balance =%d' %self.bal)
 def wit(self):
     amount=int(input('Enter amount to withdraw:'))
     if(amount>self.bal):
        print('Not enough Balance!!!')
     else:
        self.bal-=amount
        print('Your Remaining Balance =%d' %self.bal)
 def enq(self):
     print('Your Balance =%d' %self.bal)
ac = Account()
ac.dep()
ac.wit()
ac.enq()
'''


'''
#Vaibhav Bhaliya    68    SEITB-B3
import math
class circle():
    def __init__(self, r):
        self.r = r
    def area(self):
        return (self.r ** 2) * math.pi
    def peri(self):
        return self.r * 2 * math.pi

r = float(input("Radius of circle is: "))
obj = circle(r)
print("Area: ", round(obj.area(), 4))
print("Perimeter: ", round(obj.peri(), 4))
'''


#Vaibhav Bhaliya    68    SEITB-B3
class Student:
    def __init__(self, nam, eid, coll, marks):
        self.nam = nam
        self.eid = eid
        self.marks = marks
        self.coll=coll
        a=marks/5
        print("Percentage:",a)
    @staticmethod
    def collegename(self,coll):
        print(coll)
s = Student("Vaibhav", 999, "Francis", 444)
print(getattr(s, 'nam'))
setattr(s, "marks", 333)
print(getattr(s, 'marks'))
print(s.marks)  

