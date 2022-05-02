'''
import math
# VAIBHAV BHALIYA  68  SEITB-B3
print('Ceil of 3.45 is: ', math.ceil(3.45))
print('Floor of 3.45 is: ', math.floor(3.45))
print('Absolute of -3.45 is: ', math.fabs(-3.45))
print('Remainder of 4/5 is: ', math.fmod(4,5))
print('Truncate of 3.45 is: ', math.trunc(3.45))
print('4th Power of 3 is: ', math.pow(3,4))
print('Square root of 25 is: ', math.sqrt(25))
print('Sine of 1.5707963 radians is: ', math.sin(1.5707963))
print('Cosine of 1.5707963 radians is: ', math.cos(1.5707963))
print('Tangent of 0 Radians is: ', math.tan(0))
print('90 Degrees to Radians is: ', math.radians(90))
print('1.5707963 Radians to Degrees is: ', math.degrees(1.5707963))
'''

'''
# VAIBHAV BHALIYA  68  SEITB-B3
a='My Name is Anthony Gonsalves, mai Duniya me Akela hu!'
print('Original String:\n\t', a)
print('Capitlize method:\n\t', a.capitalize())
print('Length of string is: ', a.__len__())
print('Count method1\n\tCount of "a" = ', a.count('a'))
print('Count method2\n\tCount of "a" starting from index=20, = ', a.count('a',20))
print('Count method3\n\tstart=10, end=30, Count of "a" = ', a.count('a',20,30))
b='-' # '\nDil bhi hai khali, ghar bhi hai khali!'
print('Join method\n\t', b.join(a))
print('Max method\n\tMax in string is: ', max(a))
print('Min method\n\tMin in string is: ', min(a))
print('output of min is blank because\n'
      '" " space is considered as min!')
print('Swapcase method\n\t', a.swapcase())
print('Lowercase method\n\t', a.lower())
print('Uppercase method\n\t', a.upper())
'''
'''
# VAIBHAV BHALIYA   68   SEITB-B3
x = 2
y = 3
print('Addition is: ', x+y)
print('Subtrxction is: ', x-y)
print('Multiplicxtion is: ', x*y)
print('Division is: ', x/y)
print('Floor Division is: ', x//y)
print('Modulo is: ', x%y)
print('Power is: ', x**y)
'''


#   Extras
'''
print('lambda function')
dou = lambda x: x*x
print('dou(5)= ',dou(5))
print()

print('Map function')
def fu1(x):
    return x*x*x
a= map(fu1, (1,2,3,4,5))
print(set(a))
print()

print('lambda within map')
tup=(10,11,12,13,14,15)
ntup=tuple(map(lambda x: x*2, tup))
print('Output is: ',ntup)
print()

print('Filter function')
def fu2(q):
    if q>=5:
        return q
y = filter(fu2, (1,2,4,5,7,8))
print('Greater than equal to 5: ',list(y))
print()

print('lambda within filter')
y=filter(lambda x:x<=0, (1,2,-3,4,-5))
print(list(y))
print()

print('reduce function')
w= reduce(lambda x,y:x+y, [1,2,3,4,5])
print(w)
print()

print('2 num as input')
def fu3(r,t):
    if r==t:
        print(r,'=',t)
    elif r>t:
        print(r,'>',t)
    elif r<t:
        print(r,'<',t)
print("relation of 4 and 5: ")
fu3(4,5)
print()
'''