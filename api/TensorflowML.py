from keras.models import Sequential, load_model
from keras.layers import Dense
import pandas as pd
import sklearn.model_selection as sk
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import platform


class ML:
    def __init__(self, theData):
        df = pd.read_csv(theData)
        self.x = pd.get_dummies(df.drop(['IsSafe', 'Site'], axis=1))
        self.y = df['IsSafe'].apply(lambda x : 1 if x==1 else 0)
        self.model = ''
        self.xTrain = ''
        self.xTest = ''
        self.yTrain = ''
        self.yTest = ''
        self.arm = 'arm' in platform.platform()

    def splitData(self):
        self.xTrain, self.xTest, self.yTrain, self.yTest = sk.train_test_split(self.x, self.y, test_size=0.2)

    def loadModel(self):
        try:
            if(self.arm):
                self.model = load_model('tfModel-arm')
            else:
                self.model = load_model('tfModel')
        except:
            pass


        if not self.model:
            self.model = Sequential()
            self.model.add(Dense(units=10, activation='relu', input_dim=len(self.xTrain.columns)))
            self.model.add(Dense(units=7, activation='relu'))
            self.model.add(Dense(units=5, activation='relu'))
            self.model.add(Dense(units=1, activation='sigmoid'))
            self.model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')
            
    def trainML(self, theEpochs):
        self.model.fit(self.xTrain, self.yTrain, epochs=theEpochs)
        if(self.arm):
            self.model.save('tfModel-arm')
        else:
            self.model.save('tfModel')

    def predictML(self):
        yHat = self.model.predict(self.xTest)
        yHat = [0 if val < 0.5 else 1 for val in yHat]
        return yHat

    def prettyPrintML(self, data):
        print('Accuracy :', accuracy_score(self.yTest, data))
        print('F1_score :', f1_score(self.yTest, data))
        print('Precision :', precision_score(self.yTest, data))
        print('Recall :', recall_score(self.yTest, data))


ml =  ML('api/trainedData.csv')

ml.splitData()
ml.loadModel()
ml.trainML(1000)
yHat = ml.predictML()
ml.prettyPrintML(yHat)