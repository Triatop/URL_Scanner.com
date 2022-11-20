from keras.models import load_model
import pandas as pd
import math

class SafeEvaluator:

    def __init__(self):
        self.model = load_model('../tfModel')

    def isSafe(self, dict):
        # zippedLists = list(zip(self.weights, (dict.values())))

        # return (sum([val1 * val2 for val1, val2 in zippedLists]) - self.th) < 0


        dictToPd = pd.DataFrame.from_dict(dict, orient='index').transpose()
        return round((self.model.predict(dictToPd))[0][0])
