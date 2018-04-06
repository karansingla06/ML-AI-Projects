#Question1

para=input()
print("\n\nthe paragraph entered is :- \n\n",para)
sen=para.split(".")

sen[len(sen)//2]="UST Global specializes in Healthcare, Retail & Consumer Goods, Banking & Financial services telecom, Media & technology, Insurance, Teansportation & Logistics and Manufacturing & Utilities"
para="".join(sen)
print("\n\nNew para after replacement is :- \n\n",para)

d={"vowels":0,"upper":0,"lower":0, "sc":0, "rw":0}
str_copy=""
str_copy+=para
for i in para:
    if i in ["a","i","o","e","u"]:
        d["vowels"]+=1
    elif i.isupper():
        d["upper"]+=1
    elif i.islower():
        d["lower"]+=1
    elif i in ["!","@","#","$","%","^","&","*","(",")","_","-","=",",","<",">","?","~",":",";"]:
        d["sc"]+=1
        str_copy=str_copy.replace(i,"")
        
print("\n\nAll counts are :- \n\n" ,d)
print("\n\nnew paragraph after removing special character is :- \n\n",str_copy)



temp1=sen[0]
temp2=sen[len(sen)-1]
sen[0]=temp2
sen[len(sen)-1]=temp1
print("\n\nNew sentence after swaping is : \n\n","".join(sen))
