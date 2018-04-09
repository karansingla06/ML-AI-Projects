import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_excel(r"C:\Users\user\Downloads\Regression_example--weekly_pepsi-sales.xlsx", sheet_name='Data')


# General way, plot scatter
# =============================================================================
# df.plot(x='Week', y='PRICE 12PK', style='o')  
# plt.title('Week vs Price 12pk')  
# plt.xlabel('weeks')  
# plt.ylabel('Price 12pk')  
# plt.show() 
# =============================================================================



week=df["Week"].values

#plt.matshow(df.corr())


#Scatter plots
plt.figure(figsize=(8,6))
plt.title('Weeks VS Price 12pk')
p12k=df["PRICE 12PK"].values
plt.plot(week,p12k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 12PK")
plt.show()
print("Correlation- \n",np.corrcoef(week,p12k))




plt.figure(figsize=(8,6))
plt.title('Week vs Cases 12pk sales')
c12k=df["CASES 12PK"].values
plt.plot(week,c12k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 12PK")
plt.show()
print("Correlation- \n",np.corrcoef(week,c12k))


plt.figure(figsize=(8,6))
plt.title('Week vs Price 18pk')
p18k=df["PRICE 18PK"].values
plt.plot(week,p18k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 18PK")
plt.show()
print("Correlation- \n",np.corrcoef(week,p18k))




plt.figure(figsize=(8,6))
plt.title('Week vs Cases 18pk sales')
c18k=df["CASES 18PK"].values
plt.plot(week,c18k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 18PK")
plt.show()
print("Correlation-\n",np.corrcoef(week,p18k))



plt.figure(figsize=(8,6))
p30k=df["PRICE 30PK"].values
plt.plot(week,p30k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("PRICE 30PK")
plt.show()
print("Correlation-\n",np.corrcoef(week,p30k))



plt.figure(figsize=(8,6))
c30k=df["CASES 30PK"].values
plt.plot(week,c30k,marker="o")
plt.xlabel("Weeks")
plt.ylabel("CASES 30PK")
plt.show()
print("Correlation-\n",np.corrcoef(week,c30k))




# show two graphs in a single *************************

# =============================================================================
# plt.figure(figsize=(8,5))
# p12k=df["PRICE 12PK"].values
# p18k=df["PRICE 18PK"].values
# plt.plot(week,p12k,marker="o") 
# plt.plot(week,p18k,marker="o") 
# plt.plot(week,p12k,marker="o")                                                                  
# plt.ylabel("PRICE 12PK")
# plt.show()
# 
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


X = np.array(df["PRICE 12PK"].values).reshape(-1,1)
#X = df[["PRICE 12PK"]].values   #different ways to do
y = df.iloc[:, [7]].values

# =============================================================================
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
# =============================================================================

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

print(regressor.intercept_)
print(regressor.coef_)

# Predicting the Test set results
y_pred = regressor.predict(X)

# Visualising the Training set results
plt.figure(figsize=(8,6))
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Price 12pk vs Cases 12pk sales')
plt.xlabel('Price 12pk')
plt.ylabel('Cases 12pk sales')
plt.show()


# between week and price 12pk
week2=df[["Week"]].values
reg2=LinearRegression()
reg2.fit(week2,X)

plt.figure(figsize=(8,6))
plt.scatter(week2, X, color = 'red')
plt.plot(week2, reg2.predict(week2), color = 'blue')
plt.title('week vs price 12pk')
plt.xlabel('week')
plt.ylabel('price 12pk')
plt.show()
p_pred=reg2.predict(100)
print("100th week predicted value pf 12pk:-",p_pred)
print(reg2.intercept_)
print(reg2.coef_)

# between week and cases 12pk

reg3=LinearRegression()
reg3.fit(week2,y)

plt.figure(figsize=(8,6))
plt.scatter(week2, y, color = 'red')
plt.plot(week2, reg3.predict(week2), color = 'blue')
plt.title('week vs cases 12pk sales)')
plt.xlabel('week')
plt.ylabel('cases 12pk sales')
plt.show()
c_pred=reg3.predict(100)
print("in 100th weeek then predicted value of cases sales 12pk:-",c_pred[0])
print(reg3.intercept_)
print(reg3.coef_)



