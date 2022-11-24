import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
#from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('poker-hand-testing/poker-hand-testing.csv')

print(dataset)

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1:]

print(y)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)

regressor.fit(x, y)

y_pred = regressor.predict(np.array([6.5]).reshape(1,1))

print(y_pred)
