import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


model=joblib.load( 'our_pridction.joblib')
print( model.predict([[31,0]]))
