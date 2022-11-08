import SafeEvaluator

def testSafe():
    testDicts = {(0,0,0,0,0) : True,
                 (0,0,1,0,0) : True,
                 (0,0,1,1,1) : False,
                 (0,1,1,1,1) : False,
                 (1,0,0,1,1) : False,
                 (1,0,1,1,1) : False,
                 (1,1,0,1,1) : False}
    print(testDicts)
    safe = SafeEvaluator.SafeEvaluator()

    for key, val in testDicts.items():
        newKey = dict((i+1, key[i]) for i in range(len(key)))
        assert safe.isSafe(newKey) == val