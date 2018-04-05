#Q1
# =============================================================================
# import re
# p= input("Enter the sentence")
# x = True
# up=0
# lw=0
# sp=0
# digits=0
# for i in p:
#     if (i.isupper()==True):
#         up+=1
#     elif (i.islower()== True):
#         lw+=1
#     elif (i.isdigit()==True):
#         digits+=1
#     else:
#         sp+=1
# 
# print("lowercase= ",lw," uppercase= ",up," digits= ",digits)
# =============================================================================



#Q3
# =============================================================================
# nterms = int(input("Enter the value of n"))
# 
# n1 = 0
# n2 = 1
# count = 0
# 
# if nterms <= 0:
#    print("enter positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence upto",nterms,":")
#    while count < nterms:
#        print(n1,end=' , ')
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count += 1
# =============================================================================


#Q2
# =============================================================================
# 
# import operator
# f= open("D:\Python_Programe\\newfile.txt","w+")
# n= int(input("Enter number of cities"))
# for i in range(n):
#     city= input("enter name of city")
#     f.write(""+city)
#     pop = (input("enter population"))
#     f.write(" \t"+pop)
#     area = (input("enter area"))
#     f.write(" \t"+area)
#     f.write("\n")
# 
# f.close()
# 
# with open('D:\Python_Programe\\newfile.txt') as f:
#     lines = [line.split(' ') for line in f]
# output = open("D:\Python_Programe\\newfile(sorted).txt", 'w')
# 
# for line in sorted(lines, key=operator.itemgetter(0)):
#     output.write(' '.join(line))
# 
# output.close()
# =============================================================================



#DATA Structures

# Dictionary


