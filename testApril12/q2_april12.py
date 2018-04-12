#karansingla
#april12_test


import pandas as pd
import operator

df=pd.read_excel("C:/Users/user/Desktop/q2.xlsx")
print("data from file-----\n",df)
name=df["Name"].values.tolist()
height=df["Height"].values.tolist()
weight=df["Weight"].values.tolist()

d={}

for i in range(5):
    temp=[]
    temp.append(height[i])
    #temp.append(weight[i])
    d[name[i]]=temp
    

sorted_x = sorted(d.items(), key=operator.itemgetter(1))
print("Students in ascending order of their heights: \n",sorted_x)


bmi=[]
for i in range(5):
    bmi.append(int((weight[i]/(height[i]**2))*10000))


df['bmi'] = bmi
#Display top 5 rows to check if everything looks good
print("After adding bmi to dataframe\n")
print(df)
#To save it back as Excel
print("the below excel save command might not work because of permission issues\n, please close the file if opened")
df.to_excel("C:/Users/user/Desktop/q2.xlsx")


print("\nAfter grouping----- \n")
print(df.groupby(['bmi','Name']).mean())

print("\nCategorizing--- \n")
for i in range(5):
    if bmi[i]>=18 and bmi[i]<=25:
        print("healthy weight: ",name[i])
        
    elif bmi[i]>25 and bmi[i]<=30:
        print("over weight: ",name[i])
    else:
        print(" obese: ",name[i])
