import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file=r'C:\Users\user\Downloads\Regression_example--weekly_pepsi-sales.xlsx'
df = pd.read_excel(file, sheet_name='Data')


# General way, plot scatter
# =============================================================================
# df.plot(x='Week', y='PRICE 12PK', style='o')  
# plt.title('Week vs Price 12pk')  
# plt.xlabel('weeks')  
# plt.ylabel('Price 12pk')  
# plt.show() 
# =============================================================================



week=df["Week"].values


#Scatter plots
plt.figure(figsize=(8,6))
p12k=df["PRICE 12PK"].values
plt.plot(week,p12k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 12PK")
plt.show()


plt.figure(figsize=(8,6))
p18k=df["PRICE 18PK"].values
plt.plot(week,p18k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 18PK")
plt.show()


plt.figure(figsize=(8,6))
p30k=df["PRICE 30PK"].values
plt.plot(week,p30k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 30PK")
plt.show()


plt.figure(figsize=(8,6))
c12k=df["CASES 12PK"].values
plt.plot(week,c12k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 12PK")
plt.show()


plt.figure(figsize=(8,6))
c18k=df["CASES 18PK"].values
plt.plot(week,c18k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 18PK")
plt.show()


plt.figure(figsize=(8,6))
c30k=df["CASES 30PK"].values
plt.plot(week,c30k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 30PK")
plt.show()






# show two graohs in a single

# =============================================================================
# plt.figure(figsize=(8,5))
# p12k=df["PRICE 12PK"].values
# p18k=df["PRICE 18PK"].values
# plt.plot(week,p12k,marker="o") 
# plt.plot(week,p18k,marker="o") 
# plt.plot(week,p12k,marker="o")                                                                  
# plt.ylabel("PRICE 12PK")
# plt.show()
# =============================================================================



# using sklearn
# =============================================================================
# X=df["PRICE 12PK"].values
# y=df["CASES 12PK"].values
# 
# from sklearn.model_selection import train_test_split  
# from sklearn.linear_model import LinearRegression 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)  
# 
# 
# regressor = LinearRegression()  
# regressor.fit(X_train, y_train) 
# 
# print(regressor.intercept_)  
# print(regressor.coef_)  
# 
# y_pred = regressor.predict(X_test)  
# df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
# =============================================================================


