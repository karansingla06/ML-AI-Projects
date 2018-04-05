#Q1
# =============================================================================
# a = ([['Rhia',10,20,30,40,50],
#            ['Alan',75,80,75,85,100],
#            ['Smith',80,80,80,90,95]])
# slice_array = [a[i][0:2] for i in range(0,3)]
# print("Sliced Array: ",slice_array)
# 
# update= ['Sam',82,79,88,97,99]
# 
# a[2]= update
# print("Updated Array : ",a)
# 
# a[0][3]= 95
# print("newly updated array : ",a)
# 
# a[0].append("73")
# a[1].append("80")
# a[2].append("85")
# print("Newly appended array : ",a)
# =============================================================================



#Q2

# =============================================================================
# def reverse(s):
#     return s[::-1]
# 
# 
# def isPalindrome(s):
#     # Calling reverse function
#     rev = reverse(s)
# 
#     # Checking if both string are equal or not
#     if (s == rev):
#         return True
#     return False
# 
# 
# file= "#Python is an interpreted high level programming language for general-purpose programming*."
# arr=[]
# fields=[]
# i=0
# flag=0
# new_string=""
# arr= file.split()
# print(arr)
# 
# print("the palindromes are: ")
# for word in arr:
# 
#     if(isPalindrome(word)==True):
#         print(word)
# 
# print("The special characters are: ")
# for ch in file:
#     if(ch=="#" or ch=="@" or ch=="!" or ch=="$" or ch=="*"):
#         print(ch)
#     elif(ch!="."):
#         new_string+=ch
# 
# new_arr=[]
# new_arr=new_string.split()
# print(new_arr)
# 
# print("repeated words are : ")
# i=0
# count=0
# for word in new_arr:
#     j=i+1
#     for x in range(j,len(new_arr)):
#         if(word==new_arr[x]):
#             count+=1
#             print(word," : ",count)
#     i+=1
#     count=0
# =============================================================================



#Q3

# =============================================================================
# A = {5, 3, 8, 6, 1}
# B = {1, 5, 3, 4, 2}
# print("A union B : ",A.union(B))
# print("A intersection B :",A.intersection(B))
# print("A - B : ", A-B)
# print("Maximum and Minimum values of A : " , max(A),min(A))
# print("Maximum and Minimum values of B : " , max(B),min(B))
# =============================================================================




#Q4

# =============================================================================
# from math import sqrt; from itertools import count, islice
# 
# def isPrime(n):
#     return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
# 
# 
# for i in range(900,1000):
#     if(isPrime(i)):
#         if str(i) == str(i)[::-1]:
#             print(i," is a Palindrome")
#         else:
#             print(i)
# =============================================================================






