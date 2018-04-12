#karansingla
#q1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

 
df=pd.read_csv("C:/Users/user/Desktop/Camera.csv",sep=';')

print(df.shape)
print(df.head())
print(df.columns)
df.dtypes


temp= ["Model","Release date","Price"]
df2=df[temp]
print("\nfirst 25 entries ---- \n")
df2.iloc[1:25,:]


print("Summary-----\n",df.describe())

print("\nPrice summary----\n",df["Price"].describe())


df3=df[df['Price'] >'1000']

plt.figure(figsize=(10,6))
plt.plot(df3['Release date'],df3['Price'])
plt.xlabel("Release date")
plt.ylabel("Price")

plt.figure(figsize=(10,6))
plt.scatter(df['Release date'],df['Model'])
plt.xlabel("Release date")
plt.ylabel("Model")

plt.figure(figsize=(10,6))
plt.scatter(df['Release date'],df['Price'])
plt.xlabel("Release date")
plt.ylabel("Price")

plt.figure(figsize=(10,6))
plt.scatter(df['Max resolution'],df['Price'])
plt.xlabel("Max resolution")
plt.ylabel("Price")

plt.figure(figsize=(10,6))
plt.scatter(df['Low resolution'],df['Price'])
plt.xlabel("Low resolution")
plt.ylabel("Price")

plt.figure(figsize=(10,6))
plt.scatter(df['Storage included'],df['Price'])
plt.xlabel("Storage included")
plt.ylabel("Price")

plt.show()


