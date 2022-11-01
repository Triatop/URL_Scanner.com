import certValidator

def test_SelfSigned():
    url = "https://cdn.redhat.com"
    cv = certValidator.CertValidator(url)
    assert (cv.processData() == 1)
def test_hostnameMismatch():
    url = "https://ev-www.redhat.com.edgekey.net"
    cv = certValidator.CertValidator(url)
    assert (cv.processData() == 1)
def test_activeCert():
    url = "https://www.google.com"
    cv = certValidator.CertValidator(url)
    assert (cv.processData() == 0)
