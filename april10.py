# question 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv("C:/Users/user/Downloads/100SalesRecords.csv")

print(df.columns.values)

print(df.iloc[:10,:10])


plt.figure(figsize=(10,8))
plt.bar(df["Country"],df["Total Profit"])
plot.show()


for i in range(0, len(df["Total Cost"].values)):
    if df.iloc[i,12]>1000000:
        print(df.iloc[i,2])
        



#question2
        
arr= np.zeros(shape=(3,3))
print(arr.shape)

arr = arr.reshape((arr.shape[0], arr.shape[1], 1))

arr=arr+5
arr-=2
arr*=5


#question3
lis1=[]
for i in range(0,4):
    lis1.append(input("Enter the marks of student"))

print(lis1)
print(max(lis1))
print("First StudentMarks  "+lis1[0])
print("Second StudentMarks "+list1[1])
print(lis1.sort())

for i in range(0,2):
    lis1.append(input("entr marks of 2students"))
    
print(lis1)


#question4

Exam_Result={'Name':['Karan','MK','DK','PK','CK'],
             'Score':[90,20,11,10,4],
             'No_of_attempts':[1,2,3,4,5],
             'Qualify':['y','y','n','n','n']}

d=pd.DataFrame(Exam_Result,index=['a','b','c','d','e'])
print(d[d['Qualify']=='y']['Name'])
print(d[(d['Score']>=20)&(d['Score']<35)]['No_of_attempts'])

import pandas as pd
df=pd.read_csv("April11Data.csv")
print(df.info())

print(df.dtypes)
print(df.columns.to_series().groupby(df.dtypes).groups)
name=list(df['Name'])
print(name)
price=list(df['ExtPrice'])
dict1={"Name":list(name),"Price":list(price)}
print(dict1)
df_new=pd.DataFrame(dict1)
print(df_new)

