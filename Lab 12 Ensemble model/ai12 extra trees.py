import pandas  
from sklearn import model_selection  
from sklearn.ensemble import RandomForestClassifier  from sklearn.ensemble import ExtraTreesClassifier 
url = "diabetes.csv"  
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi',  'age','class']  
dataframe = pandas.read_csv(url, names=names)
dataframe = dataframe.iloc[1:] 
array = dataframe.values  
X = array[:,0:8]  
Y = array[:,8] 
seed = 7  
num_trees = 100  
max_features = 7  
kfold = model_selection.KFold(n_splits=10)  
model = ExtraTreesClassifier(n_estimators=num_trees,  
max_features=max_features)  
results = model_selection.cross_val_score(model, X, Y, 

cv=kfold)  print(results)  
print(results.mean())
