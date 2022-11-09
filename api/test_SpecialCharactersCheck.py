from SpecialCharactersCheck import SCCheck

def test_getData():
    sc = SCCheck()
    url = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    assert(sc.setData(url))
    assert(sc.l_URL == url)
    return

def test_checkAtSign():
    sc = SCCheck()
    url_t = 'https://www.youtube.com/@watch?v=NB-1zm9z3z0'
    url_f = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    sc.setData(url_t)
    assert(sc.checkAtSign() == True)
    assert(sc.value == 1)
    sc = SCCheck()
    sc.setData(url_f)
    assert(sc.checkAtSign() == False)
    assert(sc.value == 0)
    return

def test_checkHyphen():                                         # Hyphen only in domain part
    sc = SCCheck()
    url_t = 'https://en.wiki-pedia.org/wiki/Hyphen'
    url_f = 'https://en.wikipedia.org/wiki/Hyp-hen'
    sc.setData(url_t)
    assert(sc.checkHyphen() == True)
    assert(sc.value == 1)
    sc = SCCheck()
    sc.setData(url_f)
    assert(sc.checkHyphen() == False)
    assert(sc.value == 0)
    return

def test_checkDoubleForwardSlash():                             # Double forwardslash in positon > 7
    sc = SCCheck()
    url_t = 'https://sitebulb.com//folder/page.html'
    url_f = 'https://sitebulb.com/folder/page.html'
    sc.setData(url_t)
    assert(sc.checkDoubleForwardSlash() == True)
    assert(sc.value == 1)
    sc = SCCheck()
    sc.setData(url_f)
    assert(sc.checkDoubleForwardSlash() == False)
    assert(sc.value == 0)
    return

def test_All():
    sc = SCCheck()
    url = 'https://www.you-tube.com//watch?v=d40qv-2As_@Y&list=PL1wr88ZxFIz_byXyxAkXuHQrJhlRORRKp&index=50&t=214s'
    sc.setData(url)
    assert(sc.checkDoubleForwardSlash() == True)
    assert(sc.checkHyphen() == True)
    assert(sc.checkAtSign() == True)
    assert(sc.value == 3)
    return