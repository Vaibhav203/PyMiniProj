''''
# Vaibhav Bhaliya   68   Seitb-b3
class Vehicle:
    def vehicle_info(self):
        pass
    def mode_of_transport(self):
        pass
class Bike(Vehicle):
    def vehicle_info(self):
        print('Class: Bike\nMethod: vehicle_info')
    def mode_of_transport(self):
        print('Class: Bike\nMethod: mode_of_transport')
class Train(Vehicle):
    def vehicle_info(self):
        print('Class: Train\nMethod: vehicle_info')
    def mode_of_transport(self):
        print('Class: Train\nMethod: mode_of_transport')
b = Bike()
b.vehicle_info()
b.mode_of_transport()
t = Train()
t.vehicle_info()
t.mode_of_transport()
'''


from multipledispatch import dispatch
#Vaibhav BHAliya   68   seitb-b3
class Calculate:
    @dispatch(int)
    def area(r):
        print("Circle: ", 3.14 * r * r)

    @dispatch(int,int)
    def area(h,l):
        print('Triangle: ', 0.5*h*l )

    @dispatch(float,float)
    def area(l,b):
        print('Rectangle: ', l * b)

c = Calculate()
c.area(5)
c.area(4,5)
c.area(4.4,5.5)
