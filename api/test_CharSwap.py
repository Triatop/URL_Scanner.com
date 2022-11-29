from CharSwap import CharSwap

def test_getData():
    test1 = 'https://www.google.com/'
    c_swp1 = CharSwap()
    c_swp1.getData(test1)

    assert(c_swp1.c_url == 'www.google.com')    #remove https:// and the final /
    return

def test_stripWWW():
    test1 = 'https://www.google.com'    #yes www.
    test2 = 'https://sv.wikipedia.org/' #No www plus other subdomain.

    c_swp1 = CharSwap()
    c_swp2 = CharSwap()

    c_swp1.c_url = list(filter(None, test1.split('/')))[1]
    c_swp2.c_url = list(filter(None, test2.split('/')))[1]

    assert(c_swp1.stripWWW() == 1)  #did it happen?
    assert(c_swp2.stripWWW() == 0)

    assert(c_swp1.c_url == 'google.com')        #did it work?
    assert(c_swp2.c_url == 'sv.wikipedia.org')  #did it do anything it shouldn't have?

    assert(c_swp1.c_url == c_swp1.sus_url)      #did it set sus url after stripping www?
    assert(c_swp2.c_url == c_swp2.sus_url)      #did it set sus url even if it didn't strip www?

    return

def test_checkSC():
    c_swp1 = CharSwap()
    c_swp2 = CharSwap()

    c_swp1.sus_url = 'göogle.com'     #accent but no special case
    c_swp2.sus_url = 'g00gle.com'     #special cases

    assert(c_swp1.checkSC() == 0)   #did it do it, should not have
    assert(c_swp2.checkSC() == 1)   #did it do it, should have

    assert(c_swp1.sus_url == 'göogle.com')  #is still incorrect?
    assert(c_swp2.sus_url == 'google.com')  #is correct?

    return

def test_stripAccents():
    c_swp1 = CharSwap()
    c_swp2 = CharSwap()

    c_swp1.sus_url = 'ǥöóğłë.com'     #accent but no normal letters (no special cases)
    c_swp2.sus_url = 'google.com'     #correct

    assert(c_swp1.stripAccents() == 1)   #did it do it, should have
    assert(c_swp2.stripAccents() == 1)   #did it try it, should have

    assert(c_swp1.sus_url == 'google.com')  #is now correct?
    assert(c_swp2.sus_url == 'google.com')  #is still correct?

    return

def test_isTop500():
    c_swp1 = CharSwap()
    c_swp2 = CharSwap()

    c_swp1.sus_url = 'google.com'
    c_swp2.sus_url = 'doeden.dk'

    assert(c_swp1.isTop500() == 1)
    assert(c_swp2.isTop500() == 0)

    return

def test_isCharSwap():
    test1 = 'https://www.google.com'    #No accents or numbers does exist in list
    test2 = 'http://www.90ö91e.com'     #Swaps and does exist in list
    test3 = 'https://döden.se'          #Swaps and doens not exist in list
    test4 = 'https://dooden.se'         #No Swaps does not exist in list

    c_swp1 = CharSwap()
    c_swp2 = CharSwap()
    c_swp3 = CharSwap()
    c_swp4 = CharSwap()

    c_swp1.c_url = list(filter(None, test1.split('/')))[1]
    c_swp2.c_url = list(filter(None, test2.split('/')))[1]
    c_swp3.c_url = list(filter(None, test3.split('/')))[1]
    c_swp4.c_url = list(filter(None, test4.split('/')))[1]

    assert(c_swp1.isCharSwap() == 0)
    assert(c_swp2.isCharSwap() == 1)
    assert(c_swp3.isCharSwap() == 0)
    assert(c_swp4.isCharSwap() == 0)

    return
