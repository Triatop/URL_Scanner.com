from SpecialCharactersCheck import SpecialCharactersCheck

def test_setData():
    sc = SpecialCharactersCheck()
    url = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    assert(sc.setData(url))
    assert(sc.l_URL == url)
    return

def test_processData():
    sc = SpecialCharactersCheck()
    url1 = "https://net-net.br/amp/"
    sc.setData(url1)
    assert(sc.processData() == 1)
    url2 = "https://meu.cartaoaprovado.net.br/amp/"
    sc.setData(url2)
    assert(sc.processData() == 2)
    url3 = "https://meu.cartaoaprovado.net.br/@amp/"
    sc.setData(url3)
    assert(sc.processData() == 3)
    url4 = "https://meu.cartaoaprovado.net.br//amp/"
    sc.setData(url4)
    assert(sc.processData() == 4)
    return