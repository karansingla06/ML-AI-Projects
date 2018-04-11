#karan

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('linregdatset.csv')

from sklearn.preprocessing import LabelEncoder
lc = LabelEncoder()
df['Department'] = lc.fit_transform(df['Department'])

X = np.array(df.iloc[:, :-1].values).reshape(-1, 4)
y = np.array(df.iloc[:, 4].values).reshape(-1, 1)

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
