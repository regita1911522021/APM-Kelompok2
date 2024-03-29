# -*- coding: utf-8 -*-
"""amd(1.1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRtTtA3WC1vPH_WFSeWrzlXrPaZZFXFY
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from google.colab import drive
df = pd.read_csv('/content/drive/My Drive/amd/pertemuan1/data.csv', usecols=['horsepower', 'price'])

df.head()

df.info()

df.describe()

df.isnull().sum()

f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
df['horsepower'].plot(kind='kde')
f.add_subplot(1,2,2)
plt.boxplot(df['horsepower'])
plt.show()

f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
df['price'].plot(kind='kde', c='g')
f.add_subplot(1,2,2)
plt.boxplot(df['price'])
plt.show()

plt.scatter(df['horsepower'], df['price'])
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Scatter Plot Horsepower vs Price')
plt.show()

df.corr()

x = df['horsepower'].values.reshape(-1,1)
y = df['price'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

lin_reg = LinearRegression()

lin_reg.fit(x_train, y_train)

print(lin_reg.coef_)
print(lin_reg.intercept_)

lin_reg.score(x_test, y_test)

y_prediksi = lin_reg.predict(x_test)
plt.scatter(x_test, y_test)
plt.plot(x_test, y_prediksi, c='r')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.title('Plot Horsepower vs Price')

lin_reg.predict([[100]])

lin_reg.predict([[150]])

lin_reg.predict([[200]])