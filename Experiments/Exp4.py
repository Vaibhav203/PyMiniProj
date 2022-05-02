
#VAIBHAV BHALIYA    68    SEITB-B3
i,j,a,b=0,0,0,0
for i in range(0,3):
    for j in range(0,3):
        if j<=i: print('*', end=" ")
    print('')
for a in range(0,2):
    for b in range(0,2):
        if a<=b: print('*', end=" ")
    print('')



'''
#VAIBHAV BHALIYA    68    SEITB-B3
a = int(input('Enter a number: '))
sum,b=a,a
print('\nSeries is: ', b, end=" ")
for i in range(0,b-1):
    c=a*10+b
    print(c, end=" ")
    a=c
    sum=sum+c
print('\n\nSum is: ', sum)
'''


'''
#VAIBHAV BHALIYA    68    SEITB-B3
a = int(input('Enter a number: '))
for i in range(0,11):
    print(a,' x ', i, ' = ', a*i)
'''


'''
#VAIBHAV BHALIYA    68    SEITB-B3
i,a,b=0,0,1
print('\nFibonacci Series is: ')
while i<=10:
    print(a, end=" ")
    c=a+b
    a=b
    b=c
    i+=1
'''

