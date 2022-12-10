import UrlController
import random
import string

def testRedirect():
    ctr = UrlController.UrlController()
    noRedirUrl = 'https://www.bth.se/canvas/'
    RedirUrl = 'https://tinyurl.com/2m8bumv7'
    badUrl = 'www.siueg'
    assert(ctr.checkRedirect(RedirUrl) == noRedirUrl)
    assert(ctr.checkRedirect(noRedirUrl) == noRedirUrl)
    assert(ctr.checkRedirect(badUrl) == badUrl)

def testValidate():
    ctr = UrlController.UrlController()
    testUrls = {'https://www.youtube.com' : True,
                    'http://www.youtube.com' : True,
                    'http://www.twich.tv' : True,
                    'htps://notAWebsite.com' : False,
                    'htt://www.amazon.com' : False,
                    'https://www.youtube......com' : False}
    for key, val in testUrls.items():
        if val == False:
            assert(ctr.validateUrl(key) == False)
        else:
            assert(ctr.validateUrl(key))


def testEncryption():
    ctr = UrlController.UrlController()
    characters = string.ascii_letters + string.digits
    tests = [''.join(random.choice(characters) for i in range(1000)) for j in range(10000)]


    for test in tests:
        assert test == ctr.decryptUrl(ctr.encryptUrl(test))
