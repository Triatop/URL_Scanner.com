import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense
import pandas as pd
import sklearn.model_selection as sk
from sklearn.metrics import accuracy_score
import main


df = pd.read_csv('api/example.csv')

x = pd.get_dummies(df.drop(['IsPhishy'], axis=1))

y = df['IsPhishy'].apply(lambda x : 1 if x==1 else 0)

xTrain, xTest, yTrain, yTest = sk.train_test_split(x, y, test_size=0.2)

#yes = pd.DataFrame.from_dict(main.main('youtube.com', report=False), orient='index').transpose() Hur datan ska se ut när man skickar in den

model = ''

try:
    model = load_model('tfModel')
except:
    pass


if not model:
    model = Sequential()
    model.add(Dense(units=10, activation='relu', input_dim=len(xTrain.columns)))
    model.add(Dense(units=5, activation='relu'))

    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

#while(1):
model.fit(xTrain, yTrain, epochs=1000)
model.save('tfModel')

yHat = model.predict(xTest)

yHat = [0 if val < 0.5 else 1 for val in yHat]


print(accuracy_score(yTest, yHat))
