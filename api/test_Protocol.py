import Protocol_URL as PURL

def test_getData():
    Pro = PURL.Protocol_URL()
    Pro2 = PURL.Protocol_URL()
    Pro3 = PURL.Protocol_URL()
    p_rätt = 'https'
    p_fel = 'http'
    p_fler = ['https','http']
    assert(Pro.getData(p_rätt))
    assert(Pro.currentProtocol == p_rätt)
    assert(Pro.secureProtocols[0] == p_rätt)
    assert(Pro2.getData(p_fler))
    assert(Pro2.currentProtocol == p_fler[0])
    assert(Pro2.secureProtocols == p_fler)
    assert(Pro3.getData(p_fel))
    assert(Pro3.currentProtocol == p_fel)
    assert(Pro3.secureProtocols[0] == p_fel)
    return

def test_isSecure():
    Pro = PURL.Protocol_URL()
    Pro2 = PURL.Protocol_URL()
    Pro3 = PURL.Protocol_URL()
    p_rätt = 'https'
    p_fel = 'http'
    p_fler = ['https','http']

    Pro.getData(p_rätt)
    Pro2.getData(p_fler)
    Pro3.getData(p_fel)

    assert(Pro.isSecure() == 0)
    assert(Pro2.isSecure() == 0)
    assert(Pro3.isSecure() == 1)

    return
