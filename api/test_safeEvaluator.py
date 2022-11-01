import SafeEvaluator

def testSafe():
    testDicts = {(0,0,0) : False,
                 (0,1,0) : False,
                 (0,0,1) : True,
                 (0,1,1) : True,
                 (1,0,0) : True,
                 (1,0,1) : True,
                 (1,1,0) : True}
    print(testDicts)
    safe = SafeEvaluator.SafeEvaluator()

    for key, val in testDicts.items():
        newKey = dict((i+1, key[i]) for i in range(len(key)))
        assert safe.isSafe(newKey) == val