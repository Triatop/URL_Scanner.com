import UrlController
import random
import string

def testRedirect():
    ctr = UrlController.UrlController()
    noRedirUrl = 'https://www.bth.se/canvas/'
    RedirUrl = 'https://tinyurl.com/2m8bumv7'
    assert(ctr.checkRedirect(RedirUrl) == noRedirUrl)
    assert(ctr.short == 1)
    assert(ctr.checkRedirect(noRedirUrl) == noRedirUrl)
    assert(ctr.short == 0)

def testValidate():
    ctr = UrlController.UrlController()
    testUrls = {'https://www.youtube.com' : '142.250.74.78',
                    'http://www.youtube.com' : '142.250.74.78',
                    'http://www.twich.tv' : '94.199.146.85',
                    'htps://notAWebsite.com' : None,
                    'htt://www.amazon.com' : None,
                    'https://www.youtube......com' : None}
    for key, val in testUrls.items():
        if val is not None:
            assert(ctr.validateUrl(key)) is not None
        else:
            assert(ctr.validateUrl(key)) is None


def testEncryption():
    ctr = UrlController.UrlController()
    characters = string.ascii_letters + string.digits
    tests = [''.join(random.choice(characters) for i in range(1000)) for j in range(10000)]


    for test in tests:
        assert test == ctr.decrytUrl(ctr.encryptUrl(test))