'''
'# VAIBHAV BHALIYA   68   SEITB-B3
def linear(a):
    b = int(input('Enter a number to search: '))
    if b in a:
        for i in range(0, len(a)):
            if a[i] == b:
                print('Element found at index: ', i)
    else:
        print('Element is not found')
a = [10,11,12,13,14,15]
linear(a)
'''


'''
# VAIBHAV BHALIYA   68   SEITB-B3
def dividebyzero():
    print('\nCannot divide by Zero!')
def divide(a,b):
    if b==0:
        dividebyzero()
    else:
        print('\nDivision is: ', a/b)
a = int(input('Enter the Numerator: '))
b = int(input('Enter the Denominator: '))
divide(a,b)
'''
'''
# VAIBHAV BHALIYA   68   SEITB-B3
def check(l):
    print("\n", l, "\n")
    for i in range(0, len(l)):
        e=l[i]
        if e[-3:]=='ing':
            e+='ly'
            l[i] = e
            print(e)
    print("\n", l, "\n")
l = ['bowling','bat','flying','elephant','sleeping','fish']
check(l)
'''
'''
# VAIBHAV BHALIYA   68   SEITB-B3
from functools import reduce
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

print('Filter function')
def fu2(q):
    if q>=5:
        return q
y = filter(fu2, (1,2,4,5,7,8))
print('Greater than equal to 5: ',list(y))
print()

print('reduce function')
w = reduce(lambda x,y:x+y, [1,2,3,4,5])
print(w)
print()
'''



'''
# VAIBHAV BHALIYA   68   SEITB-B3
class Iterat(object):
    def __init__(self, low, high):
        self.cur = low
        self.high = high
    def __iter__(self):
        'Return itself as an iterator object'
        return self
    def __next__(self):
        'Return the next value till current is lower than high'
        if self.cur > self.high:
            raise StopIteration
        else:
            self.cur += 1
            return self.cur - 1
a = Iterat(4, 10)
for i in a:
    print(i)
l = ['a', 'b', 1, 2, 3]
print(l, '\n')
it1 = iter(l)
print(iter(it1))
print(iter(it1))
print(iter(it1))
print()
t = ('As', 'Df', 123)
it2 = iter(t)
print(next(it2))
print(next(it2))
print(next(it2))
print()
s = 'My Name is Anthony Gonsalves!'
it3 = iter(s)
print(next(it3))
print(next(it3))
print(next(it3))

def generate():
    s1 = 'Hello'
    yield s1
    num = 45
    yield num
    num += 10
    yield num

for i in generate():
    print(i)
'''


# VAIBHAV BHALIYA   68   SEITB-B3
def recur(a):
    if a<=0:
        return a
    else:
        return a+recur(a-1)
print(recur(5))
