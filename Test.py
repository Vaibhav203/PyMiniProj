from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame()

df['Name']=['Raja','Krishnaappa','Beria','Monster','Rocky','Bhai','Sultan','Maalik']
df['Roll'] = ['12','13','14','15','16','17','18','19']
df['Gender'] = ['Male','Male','Male','Male','Male','Male','Female','Male']
df['Age'] = ['18','19','20','28','26','26','27','29']
df['Marks'] = ['40','45','44','48','49','42','46','47']

a,b=0,0
for s in df['Gender']:
    if s=='Male':
        a+=1
    if s=='Female':
        b+=1

plt.pie([a,b], colors=['red','orange'],autopct='%0.2f%%',startangle=90)
plt.legend(labels=['Male','Female'],loc='lower right')
plt.show()

w,v=[],[]
for i in df['Marks']:
    v.append(int(i))
for j in df['Name']:
    w.append(j)

plt.plot(w,v)
plt.tight_layout()
plt.show()


