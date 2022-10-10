import PortCheck as pc

def testPortCheck():
    testIPs = {'216.58.211.14' : '443',
               '151.101.86.167' : '443', 
               '192.168.0.1' : None}
    check = pc.PortCheck()
    for key, val in testIPs.items():
        assert check.checkPorts(key) == val