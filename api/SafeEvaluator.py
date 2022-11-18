from keras.models import load_model
import pandas as pd

class SafeEvaluator:

    def __init__(self):
        self.model = load_model('../tfModel')
        self.weights = (7, 2, 4, 3, 5)
        self.th = 6

    def isSafe(self, dict):
        # zippedLists = list(zip(self.weights, (dict.values())))

        # return (sum([val1 * val2 for val1, val2 in zippedLists]) - self.th) < 0


        dictToPd = pd.DataFrame.from_dict(dict, orient='index').transpose()
        return (self.model.predict(dictToPd))
