# import pandas as pd
# from matplotlib import pyplot as plt

# data = pd.read_csv("graduate_data.csv")
# frame = pd.DataFrame(data)
#
# male = frame['Men'][0]
# female = frame['Women'][0]
# plt.pie([male,female], autopct="%0.2f%%")
# plt.legend(labels=['Male','Female'],loc='lower right')
# plt.title('Petroleum Engineering Male Female Workers')
# plt.tight_layout()
# plt.show()
#
# rate1 = frame['Unemployed'][5]
# rate2 = frame['Unemployed'][8]
# rate3 = frame['Unemployed'][12]
# rate4 = frame['Unemployed'][18]
# rate = [rate1,rate2,rate3,rate4]
#
# plt.bar(['Nuclear','Mechanical','Biomedical','Architectural'],rate)
# plt.title('Engineering Unployment')
# plt.tight_layout()
# plt.show()
#
# emp = frame[10:15]['College_jobs']
# plt.hist(emp, bins=[5500,6000,6500,7000,7500,8000,8500,9000])
# plt.title('College Jobs Provided')
# plt.tight_layout()
# plt.show()
#
# w = frame[5:10]['Women']
# plt.plot(['Nuclear','Actuarial','Astronomy','Mechanical','Electrical'],w)
# plt.title('Women in Different Sectors')
# plt.show()


'''
import numpy as np
import pandas as pd

dict = {'Days':['1','2','3','4','5'],'Tip':[100,200,350,150,250]}
df = pd.DataFrame.from_dict(dict)
print(df)
'''


'''
import numpy as np
import pandas as pd

dict = {'Days':['1','2','3','4','5'],'Tip':[100,200,350,150,250]}
df = pd.DataFrame.from_dict(dict)
print(df)
a = []
for i in df['Tip']:
    a.append(i)

print("\nMax Tip: ",max(a))
print("Min Tip: ",min(a))
print("Mean Tip: ",np.mean(a))
print("Median of Tip: ",np.median(a))
print("Total Tip: ",np.sum(a))

'''
