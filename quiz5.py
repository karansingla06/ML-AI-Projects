#question 1

import numpy as np
from sklearn.linear_model import LinearRegression

X1= np.array([1901,1911,1921,1931,1941,1951,1961,1971,1981,1991,2001]).reshape(-1,1)
y1= np.array([236,258,251,272,319,361,439,548,685,843,1027]).reshape(-1,1)

clf= LinearRegression()
clf.fit(X1,y1)

x_test=np.array([2011,2021,2031]).reshape(-1,1)
y_pred=clf.predict(x_test)

print(y_pred)


#question 2
#A)

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df=pd.read_excel("C:/Users/user/Desktop/income.xlsx")
print("total missing values:\n",df.isnull().sum())
df=df.apply(lambda x:x.fillna(x.value_counts().index[0]))


df2=pd.get_dummies(df,columns=['Employment','Marital_status','Gender'])
df2['Income']=np.where(df['Income']=='<5 Lakhs',0,1)
df2.shape
df2=df2.reindex(['Age','Employment_Govt','Employment_Private','Employment_Self Employed','Marital_status_married','Marital_status_single','Gender_F','Gender_M','Income'],axis=1)

X2= df2.iloc[:,:8]
y2=df2.iloc[:,8]
clf2= LogisticRegression()
clf2.fit(X2,y2)

df2.head()
y_pred= clf2.predict([[28,0,1,0,0,1,1,0],[30,1,0,0,1,0,0,1]])
print("Predicted values for the given input-\n",y_pred)


#B)

df3=df
df3=df3.drop('Age',axis=1)

from sklearn.preprocessing import LabelEncoder
df3=df3.apply(LabelEncoder().fit_transform)

df3['Age']=df['Age']
df3=df3.reindex(['Age','Employment','Marital_status','Gender','Income'],axis=1)

from sklearn.naive_bayes import GaussianNB
clf3=GaussianNB()
X3=df3.iloc[:,:4]
y3=df3.iloc[:,4]
clf3.fit(X3,y3)

y_pred2= clf3.predict([[28,1,1,0],[30,0,0,1]])

print("Predicted values for the given input-\n",y_pred2)



#C)

age=df3.Age.values.tolist()
emp=df3.Employment.values.tolist()
ms=df3.Marital_status.values.tolist()
gen=df3.Gender.values.tolist()
temp2=[]
attr=[[]]
for i in range(len(age)):
    temp2.append([age[i],emp[i],ms[i],gen[i]])
    attr.append(temp2[i])
attr.pop(0)

keys=[1,2,3,4,5,6,7,8,9,10,11]

d=dict(zip(keys,attr))
print(d)

def EucDis(m,n):
    return (((m[0]-n[0])**2) + ((m[1]-n[1])**2) +((m[2]-n[2])**2) +((m[3]-n[3])**2))**0.5
    
ini_cluster=[]
f_cluster=[]
cents=[]

import random
rc= random.sample(d.keys(),2)

for i in rc:
    f_cluster.append([i])
    cents.append(d[i])

flag=True
while flag:
    p_cluster=f_cluster
    for key,val in d.items():
        ind=0
        dis1=10000000
        
        for i in range(len(cents)):
            if dis1>EucDis(val,cents[i]):
                dis1=EucDis(val,cents[i])
                ind=i
        
        if key not in f_cluster[ind]:
            f_cluster[ind].append(key)     
    if p_cluster==f_cluster:
        flag=False        
print("Clusters are- \n",f_cluster)
    

    
    



