from URLLength import LengthURL

def test_getData():
    lu = LengthURL()
    url = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    assert(lu.getData(url))
    assert(lu.l_URL == url)
    return

def test_isURLLong():
    lu = LengthURL()
    url1 = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    url2 = 'https://www.youtube.com/watch?v=d40qv-2As_Y&list=PL1wr88ZxFIz_byXyxAkXuHQrJhlRORRKp&index=50&t=214s'
    lu.getData(url1)
    assert(lu.isURLLong() == False)
    lu.getData(url2)
    assert(lu.isURLLong() == True)
    return

def test_URLLong():
    lu = LengthURL()
    url1 = 'https://www.youtube.com/watch?v=NB-1zm9z3z0'
    lu.getData(url1)
    assert(lu.URLLong() == len(url1))
    return