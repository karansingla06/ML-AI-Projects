#Q1

# =============================================================================
# def digit_list(i):
#     temp=[]
#     while i!=0:
#         rem=i%10
#         temp.append(rem)
#         i=i//10
# 
#     sumi=0
#     st=""
#     for j in temp:
#         sumi+=j**3
#     
#     if sumi==int(st.join(str(x) for x in temp[::-1])):
#         return True
#     
#         
# 
# 
# for i in range(1,1001):
#     if digit_list(i):
#         print(i)
#             
#             
# =============================================================================



#Q2
# =============================================================================
# import numpy
# A =[[3, 5, 6], [4, 8, 10],[2, 1, 8]]
# I = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
# 
# m=numpy.matmul(A,I)
# print(m)
# if m.tolist()==A:
#     print("proved A=A.I")
# =============================================================================
    
  
  
#Q3
# =============================================================================
# d={}
# n=int(input("Please enter value of n: "))
# for i in range(1,n+1):
#     d[i]=i**i
# print(d)
# =============================================================================



#Q4

# =============================================================================
# sen=input()
# l_count=0
# d_count=0
# for i in sen:
#     if i.isdigit():
#         d_count+=1
#     elif i.isalpha():
#         l_count+=1
# print(d_count,l_count)
# 
# =============================================================================




#Q5

# =============================================================================
# import math
# 
# def factorial(i):
#     return math.factorial(i)
# def lcm(i,j):
#     return abs(i*j)/math.gcd(i,j)
# def hcm(i,j):
#     return math.gcd(i,j)
# def factors(i):
#     i=1
#     f=[]
#     while i<=math.sqrt(n):
#         if n%i==0:
#             if n/i==i:
#                 f.append(i)
#             else :
#                 f.append(i)
#                 f.append(n//i)
#         i=i+1
#     return f
# 
# 
# inp=int(input("enter the number, 1 for factorial, 2 for lcm, 3 for hcm, 4 for factors: "))
# 
# if inp==1 or inp==4:
#     n=int(input("enter a number: "))
#     if inp==1:
#         print(factorial(n))
#     elif inp==4:
#         print(factors(n))
# elif inp==2 or inp==3:
#     n,m=map(int,input("enter two numbers: ").split())
#     if inp==2:
#         print(lcm(n,m))
#     elif inp==3:
#         print(hcm(n,m))
# else:
#     print("wrong input")
# =============================================================================























