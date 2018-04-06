#question2

import numpy as np

names=[]
sub1=[]
sub2=[]
sub3=[]
total=[]
for i in range(10):
    names.append(input("enter name of student: "))
    x,y,z= map(int,input("enter marks for 3 subjects: ").split())
    sub1.append(x)
    sub2.append(y)
    sub3.append(z)

print(names,"\n",sub1,"\n",sub2,"\n",sub3,"\n")

mean_sub1= np.mean(sub1)
mean_sub2= np.mean(sub2)
mean_sub3= np.mean(sub3)

med_sub1=np.median(sub1)
med_sub2=np.median(sub2)
med_sub3=np.median(sub3)

print("Means are for sub1,2,3: ",mean_sub1,mean_sub2,mean_sub3)
print("Medians are for sub1,2,3: ",med_sub1,med_sub2,med_sub3)

d={}
for i in range(10):
    d[names[i]]=(sub1[i]+sub2[i]+sub3[i])/3
    


for i in d:
    if d[i]>90:
        print(i,":","A+")
    elif d[i]>80 and d[i]<=90:
        print(i,":","A")
    elif d[i]>70 and d[i]<=80:
        print(i,":","B+")
    elif d[i]<70:
        print(i,":","B")
        
