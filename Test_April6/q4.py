# question 4

d={"children":[],"youth":[],"middle-aged":[],"senior":[]}
for _ in range(20):
    name=input("enter name")
    age=int(input("enter age"))
    if age<15:
        d["children"].append(name)
    elif age>=15 and age<30:
        d["youth"].append(name)
    elif age>=30 and age<50:
        d["middle-aged"].append(name)
    else:
        d["senior"].append(name)
print(d)

