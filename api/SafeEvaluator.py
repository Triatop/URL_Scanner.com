class SafeEvaluator:

    def __init__(self):
        self.attributes = (5, 2, 4)
        self.th = 3

    def isSafe(self, dict):
        zippedLists = list(zip(self.attributes, (dict.values())))

        return (sum([val1 * val2 for val1, val2 in zippedLists]) - self.th) > 0
