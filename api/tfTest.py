import tensorflow as tf
from keras.models import Sequential, load_model
from keras.layers import Dense
import pandas as pd
import json
import sklearn.model_selection as sk


with open('api/testingData.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='index')

test, train = sk.train_test_split(df, test_size=0.2, train_size=0.2)



# model = Sequential()
# model.add(Dense(units=32, activation='relu', input_dim=len(train.columns)))
# model.add(Dense(units=64, activation='relu'))
# model.add(Dense(units=32, activation='relu'))
# model.add(Dense(units=1, activation='sigmoid'))

# model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

# model.fit(train, train, None, epochs=30)


# yes = pd.DataFrame.from_dict({'www.oogabooga.com': True}, orient='index')

