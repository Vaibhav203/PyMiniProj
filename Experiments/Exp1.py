'''
# Numeric Datatypes
# Vaibhav Bhaliya 68 Seit-B3
a=12
b=12.1212
c=12+23j
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print("Type of c: ", type(c))
print("conversion of a to float: ", type(float(a)))
print("conversion of b to complex: ", type(complex(b)))
'''

'''
# Methods of List
# Vaibhav Bhaliya 68 Seit-B3
l=[1,2,3,4,5,9,8,7,6]
m=[10,11,12]
l.append(77)
print("\nAppending '77'", l)
l.insert(2, 99)
print("Inserting 99 at Index 2", l)
print("Index of '4' is: ", l.index(4))
print("Counting '8' is: ", l.count(8))
l.remove(99)
print("Removing 99", l)
l.reverse()
print("Reversing.....", l)
l.sort()
print("Sorting.....", l)
print('sum is: ', sum(l))
l.extend(m)
print('extending l by(10,11,12): ', l)
print('length is: ', l.__len__())
'''

'''
# Methods of Tuple
# Vaibhav Bhaliya 68 Seit-B3
d=( 12, 34, 33, 67, 56, 76, 99,90,100)

print('Tuple is: ')
for x in d:
    print(x)
print('Count of 12 is: ', d.count(12))
print('Length is: ', len(d))
print('Min is: ', min(d))
print('Max is: ', max(d))
print('Sort is: ', sorted(d))
print('Reverse sort is: ', sorted(d, reverse=True))
print('Index of 56 is: ', d.index(56))
print('Index of 56 from index 3 is: ', d.index(56, 3)  )
print('Index of 56 between index 4 to 8 is: ', d.index(56, 2, 8))
'''

'''
# Methods of Dictionary
# Vaibhav Bhaliya 68 Seit-B3
dict={'Name':'MyName', 'Age':19, 'Class':'Seitb3', 'School':'MySchool'}
print("Name: ", dict['Name'])
print("Type representation: ", type(dict))
print('Items are: ',dict.items())
print("Keys: ", dict.keys())
print("Values: ", dict.values())
dict['Age']=20
print("After changing: Age is ", dict['Age'])
print('Deleting School')
del dict['School']
print('Successfully Deleted')
dict.update({'School':'Francis'})
print('After Updation: ',dict.items())
print("String representation: ", str(dict))
print("Type representation: ", type(str(dict)))
print('Popping: ', dict.pop('School'))
print('Dict after popping: ', dict.items())
a={'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f',}
b={'C':'c', 'D':'d', 'A':'a',}
print('Checking for common keys in 2 dictionaries')
for keys in a.keys():
    if keys in b.keys():
        print('checking for: ',keys)
        print('key is PRESENT in b')
    else:
        print('checking for: ',keys)
        print('key is ABSENT in b')
print()
'''

'''
#range function
# Vaibhav Bhaliya 68 Seit-B3
l=[10,20,30,40,50,60,70,80,90,100]
print("method 1: range(1 parameter)")
for a in range(5):
    print(l[a], end=" ")
print("\nmethod 2: range(2 parameters)")
for a in range(5, 10):
    print(l[a], end=" ")
print("\nmethod 3: range(3 parameters)")
for a in range(0,9,2):
    print(l[a], end=" ")
'''

'''
# Methods of Sets
# Vaibhav Bhaliya 68 Seit-B3
empty=set()
print("Empty Set: ", empty)
x={"Name", "Age", "Class", "Age"}
print("Is Age in set? ", 'Age' in x)
print('contents of set: ')
for y in x:
    print(y, end=" ")
print('\n',x)
x.add("School")
print("Added School: ", x)
x.remove("Class")
print("Remove Class: ", x)
x.pop()
print("Popped: ", x)
print("\nClearing set using clear() method: ")
x.clear()
print("cleared set, structure is retained")
print('deleting.....')
del x
print("Deleted the set completely")
print("In new sets x and y... ")
y={'X','Y','A','B'}
x={'A','B','C','D','E'}
print("Min: ", min(x))
print("Max: ", max(x))
x.update(['F','G','H'])
print("Updated String: ", x)
print("Union: ", x.union(y))
print("Intersection: ", x.intersection(y))
print("Intersection: ", x&y)
print("Union: ", x|y)
print("Difference: ", x-y)
print("OR: ", x^y)
print("Symetric diference: ", x.symmetric_difference(y))
print("Symetric diference of Symetric diference: ",
      x.symmetric_difference(x.symmetric_difference(y)))
print("Union: ", x.union(y))
print("membership")
print("A is member of x? ", 'A' in x)
print("X is member of x? ", 'X' in x)
print("subsets")
print("x is subset of y? ", x.issubset(y))
print("x is superset of y? ", x.issuperset(y))
print("conversions")
print("set to tuple: ", tuple(x), type(tuple(x)))
print("set to list: ", list(x), type(set(x)))
'''

'''
# Extra problem
# Vaibhav Bhaliya 68 Seit-B3

d=(1,2,3,4,5,6,7,8,9)
for x in d:
    if(d.index(x)==3):
        print('4th from first position: ')
        print(x)
    if(d.index(x)==(len(d)-4)):
        print('4th position from last: ')
        print(x)

c=(1,2,3,4,5,6,7,8,8,9)
for item in c:
    if c.count(item)>1:
        print(item)
'''