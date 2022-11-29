from MaliciousLinks import MaliciousLinks

def test_getNrOfMalLinks():
    m_al = MaliciousLinks()
    assert(m_al.getNrOfMalLinks() == 0)
    m_al.m_NrOfMalLinks = 3
    assert(m_al.getNrOfMalLinks() == 3)
    return

def test_getData():
    m_al = MaliciousLinks()
    url1 = 'https://thepiratebay.org/'
    urls = ['https://www.garykessler.net/library/file_sigs.html', 'https://www.youtube.com/', 'https://github.com/']
    assert(m_al.getData(url1, urls) == 1)
    assert(m_al.m_url == list(filter(None, url1.split('/')))[1])
    assert(m_al.m_links == urls)
    return

def test_externalCheck():
    m_al = MaliciousLinks()
    url1 = 'https://www.youtube.com/'
    urls = ['https://mail.google.com/mail/u/0/#inbox', 'https://www.youtube.com/feed/subscriptions', 'https://www.youtube.com/feed/history', 
            'https://www.google.com/', 'https://github.com/', '/info', '//www.youtube.com'] #/is a relative link(internal) //is a link with unspecified protocol

    comp = ['https://mail.google.com/mail/u/0/#inbox', 'https://www.google.com/', 'https://github.com/']
    m_al.getData(url1, urls)
    assert(m_al.externalCheck() == 1)
    assert(m_al.m_links == comp)
    return

def test_removeDup():
    m_al = MaliciousLinks()
    url1 = 'https://thepiratebay.org/'
    urls = ['https://www.youtube.com/feed/subscriptions', 'https://www.youtube.com/feed/history', 'https://www.google.com/', 'https://github.com/']
    comp = ['https://www.youtube.com/feed/subscriptions', 'https://www.google.com/', 'https://github.com/']
    m_al.getData(url1, urls)
    assert(m_al.removeDup() == 1)
    assert(m_al.m_links == comp)
    return

def test_maliciousCheck():
    m_al = MaliciousLinks()
    url1 = 'https://twitter.com/'
    urls = ['https://www.youtube.com/', 'https://www.google.com/']
    m_al.getData(url1, urls)
    assert(m_al.maliciousCheck()) #Does not test against a hard coded value. Impossible to hard code due to one of the objects returned being current time.
    return

def test_isExternalSafe():
    m_al1 = MaliciousLinks()
    m_al2 = MaliciousLinks()
    url1 = 'https://twitter.com/'
    mal_urls = ['https://italarizege.xyz/redirect?tid=855295', 'https://festivalesperu.site/']
    saf_urls = ['https://www.youtube.com/', 'https://www.google.com/', '//www.google.com/', '//facebook.com']
    m_al1.getData(url1, mal_urls)
    m_al2.getData(url1, saf_urls)
    assert(m_al1.isExternalSafe() == 0)
    assert(m_al2.isExternalSafe() > 0)
    return
