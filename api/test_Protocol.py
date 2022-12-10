import Protocol_URL as PURL

def test_getData():
    Pro = PURL.Protocol_URL()
    p_correct = 'https'
    p_incorrect = 'http'
    p_more = ['https','http']
    assert(Pro.getData(p_correct))
    assert(Pro.currentProtocol == p_correct)

    assert(Pro.getData(p_more))
    assert(Pro.currentProtocol == p_more[0])
    
    assert(Pro.getData(p_incorrect))
    assert(Pro.currentProtocol == p_incorrect)
    return

def test_isSecure():
    Pro = PURL.Protocol_URL()
    p_correct = 'https'
    p_incorrect = 'http'
    p_more = ['https','http']


    Pro.getData(p_correct)
    assert(Pro.isSecure() == 1)
    Pro.getData(p_more)
    assert(Pro.isSecure() == 1)
    Pro.getData(p_incorrect)
    assert(Pro.isSecure() == 0)

    return
