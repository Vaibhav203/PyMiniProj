'''
import numpy as np
from array import *
# VAIBHAV BHALIYA   68   SEITB-B3
aa = np.array([('A',1,1.1),('B',2,2.2),('C',3,3.3),('D',4,4.4),('E',5,5.5),('F',6,6.6)])
print('\nArray with multiple datatypes: \n', aa)
print('')
a=array("d", [2.1,8.1,7.1,3.1])
print(a)
print('Element at index 2 is: ', a[2])
print('Length is:             ', len(a))
a.append(2.2)
print('Appending 2.2:         ', a)
a.extend([7.7,8.8,9.9])
print('Extending 7.7,8.8,9.9: ',a)
a.insert(2,5.567)
print('Inserting 5.567 at 2:  ', a)
'''


'''
#implement stack using array

import array as aa
# VAIBHAV BHALIYA   68   SEITB-B3
arr = aa.array('d', [1,5,9,2,7])
print('')
for i in range (0, arr.__len__()):
    print(' ',arr[i],' ', end=" ")
a=1
while a in range(1,3):
    a = int(input('\n\n1 to Push\n2 to Pop\n3 to Exit\n\tChoice: '))
    if a==1:
        b=int(input('Enter number to Push: '))
        arr.append(b)
        for i in range(0, arr.__len__()):
            print(' ',arr[i],' ', end=" ")
    if a==2:
        arr.pop(arr.__len__()-1)
        for i in range(0, arr.__len__()):
            print(' ',arr[i],' ', end=" ")
    if a==3:
        print('Exiting')
'''





import numpy as np
# VAIBHAV BHALIYA   68   SEITB-B3
print('\nProperties of Numpy Array')
zeroarray=np.zeros((3,2))
print('zero_array= ', zeroarray)
onearray=np.ones((3,2))
print('ones_array= ', onearray)
q=np.arange(9).reshape(3,3)
print('q= ', q)
print('Transpose of q= ', q.transpose())



'''
import numpy as np
# VAIBHAV BHALIYA   68   SEITB-B3
a=np.array([[1,0],[6,4]])
print('\nMultidimensional Array is: ',a)
z=np.array([[1,6,7], [5,9,2],[3,8,4]])
print("Element at z[1][2] is: ",z[1][2])
print('z[0]: ',z[0])
print('z[1]: ',z[1])
print('z[-1]: ',z[-1])
print('z[-2]: ',z[-2])
print('z[:,0]: ',z[:,0])
print('z[:,2]: ',z[:,2])
print('z[:,-1]: ',z[:,-1])
'''