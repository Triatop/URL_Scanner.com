import PortCheck as pc

def testPortCheck():
    testIPs = {'216.58.211.14' : [True, 'https'],
               '151.101.86.167' : [True, 'https'], 
               '192.168.0.1' : [False, 'https']}
    check = pc.PortCheck()
    for key, val in testIPs.items():
        assert check.checkPorts(key, val[1]) == val[0]