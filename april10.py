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



