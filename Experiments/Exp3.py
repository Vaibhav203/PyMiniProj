# VAIBHAV BHALIYA   68   SEITB-B3
print('Calculator\n')
def add(x,y):  return x+y
def sub(x,y):  return x-y
def mul(x,y):  return x*y
def div(x,y):  return x/y
for c in range(0,5):
    c=int(input('\t1 to Add\n\t2 to Subtract\n\t3 to Multiply\n\t4 to Divide\n\t5 to Exit\n\tEnter: '))
    if c==1:
        a=int(input('Enter 1st Number: '))
        b=int(input('Enter 2nd Number: '))
        print('Addition is: ', add(a,b),'\n')
    elif c==2:
        a=int(input('Enter 1st Number: '))
        b=int(input('Enter 2nd Number: '))
        print('Subtraction is: ', sub(a,b),'\n')
    elif c==3:
        a=int(input('Enter 1st Number: '))
        b=int(input('Enter 2nd Number: '))
        print('Multiplication is: ', mul(a,b),'\n')
    elif c==4:
        a=int(input('Enter 1st Number: '))
        b=int(input('Enter 2nd Number: '))
        print('Division is: ', div(a,b),'\n')
    else:
        print('Exited')



'''
a = int(input('Enter a random number: '))
if a>0: print('It is POSITIVE')
elif a<0: print('It is NEGATIVE')
else: print('It is neither POSITIVE nor NEGATIVE (= 0)')
'''


'''
a = int(input('Enter a year: '))

if (a%400==0) or (a%4==0 and a%100!=0):
    print("Entered year is leap year")
else:
    print("Entered year is not leap year")
'''

'''
# VAIBHAV BHALIYA   68   SEITB-B3
a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
print('')
if a>b:
    if a>c:
        print('Greatest Number: ', a)
    elif a<c:
        print('Greatest Number: ', c)
    else:
        print('Greatest Number: ', a)
elif a<b:
    if b>c:
        print('Greatest Number: ', b)
    elif b<c:
        print('Greatest Number: ', c)
    else:
        print('Greatest Number: ', b)
else:
    if b > c:
        print('Greatest Number: ', b)
    elif b < c:
        print('Greatest Number: ', c)
    else:
        print('Greatest Number: ', b)
'''