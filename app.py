import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

music_file='music.csv'

# loading data
music_dt  =pd.read_csv(music_file)

# prepare 2 groups (features, output)
X=music_dt.drop(columns=['genre']) # sample features (age,gender) -X
Y=music_dt['genre'] # sample output - Y -genre

# X= input train,test, Y = output train, testing
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=.2)

model = DecisionTreeClassifier()

model.fit(X_train,Y_train) # load features and sample data
# model.fit(X,Y) # load features and sample data

predictions= model.predict(X_test) # make prediction base on the features and 

joblib.dump(model, 'our_pridction.joblib') #binary file

# score=accuracy_score(Y_test,predictions)
# print(score)
# predictions= model.predict([[16,1],[22,0]]) # make prediction base on the 
# print(predictions)


# print(Y)
# 0 - famale
# 1 - male