import pandas as pd 
import numpy as np 
from sklearn import model_selection  
from sklearn.ensemble import BaggingClassifier  
from sklearn.tree import DecisionTreeClassifier  
url = "diabetes.csv" 
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',  'age','class']  
dataframe = pd.read_csv(url, names=names)  
dataframe = dataframe.iloc[1:] 
array = dataframe.values  
X = array[:,0:8]  
Y = array[:,8]  
seed = 7 
kfold = model_selection.KFold(n_splits=10, random_state=seed,  shuffle=True)  
cart = DecisionTreeClassifier()  
num_trees = 100  
dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True) model = BaggingClassifier(base_estimator=cart, n_estimators=num_trees,  random_state=seed)  
results = model_selection.cross_val_score(model, X, Y, cv=kfold,  error_score='raise')  
print(results)  
print(results.mean()) 
