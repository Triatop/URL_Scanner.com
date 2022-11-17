class SafeEvaluator:

    def __init__(self):
        self.weights = (7, 2, 4, 3, 5, 2, 4)
        self.th = 6

    def isSafe(self, dict):
        zippedLists = list(zip(self.weights, (dict.values())))

        return (sum([val1 * val2 for val1, val2 in zippedLists]) - self.th) < 0
