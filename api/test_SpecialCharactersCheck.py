from SpecialCharactersCheck import SCCheck

def test_setData():
    sc = SCCheck()
    url = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    assert(sc.setData(url))
    assert(sc.l_URL == url)
    return

def test_processData():
    sc = SCCheck()
    url1 = "https://net-net.br/amp/"
    sc.setData(url1)
    sc.processData()
    assert(sc.sev == 1)
    url2 = "https://meu.cartaoaprovado.net.br/amp/"
    sc.setData(url2)
    sc.processData()
    assert(sc.sev == 2)
    url3 = "https://meu.cartaoaprovado.net.br/@amp/"
    sc.setData(url3)
    sc.processData()
    assert(sc.sev == 3)
    url4 = "https://meu.cartaoaprovado.net.br//amp/"
    sc.setData(url4)
    sc.processData()
    assert(sc.sev == 4)
    return