#Q1
# =============================================================================
# import numpy as np
# 
# from scipy import stats
# rent=[]
# for _ in range(10):
#     rent.append(int(input()))
#     
# meani= np.mean(rent)
# mediani=np.median(rent)
# modei=stats.mode(rent,axis=None)
# 
# print(meani,mediani,modei.mode[0])
# freq_table=stats.itemfreq(rent)
# print("frequencyy table list : ",freq_table)
# print("cum frequency list: ",stats.cumfreq(rent))
# 
# print("25th percentile is "+np.percentile(rent,25))
# print("50th percentile is "+np.percentile(rent,50))
# print("75th percentile is "+np.percentile(rent,75))
# print("variance is", np.var(rent))
# print("cov is : ",stats.variation(rent))
# =============================================================================



#Q3

# =============================================================================
# exp=input()
# operand=[]
# operator=[]
# for i in exp:
#     if i.isdigit():
#         operand.append(i)
#     elif i=="(":
#         operator.append(i)
#     else:
#         operator.append(i)
# print(operand,operator)  
# 
# =============================================================================

# =============================================================================
# 
# OPERATORS = set(['+', '-', '*', '/', '(', ')'])
# PRIORITY = {'+':1, '-':1, '*':2, '/':2}
# 
# def infix_to_postfix(formula):
#     stack = [] # only pop when the coming op has priority 
#     output = ''
#     for ch in formula:
#         if ch not in OPERATORS:
#             output += ch
#         elif ch == '(':
#             stack.append('(')
#         elif ch == ')':
#             while stack and stack[-1] != '(':
#                 output += stack.pop()
#             stack.pop() # pop '('
#         else:
#             while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
#                 output += stack.pop()
#             stack.append(ch)
#     # leftover
#     while stack: output += stack.pop()
#     return output
# 
# def evaluate_postfix(formula):
#     stack = []
#     for ch in formula:
#         if ch not in OPERATORS:
#             stack.append(float(ch))
#         else:
#             b = stack.pop()
#             a = stack.pop()
#             c = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}[ch]
#             stack.append(c)
#     return stack[-1]
# 
# 
# exp=input()
# postfx=infix_to_postfix(exp)
# print(evaluate_postfix(postfx))
# =============================================================================

