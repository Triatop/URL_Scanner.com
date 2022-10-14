import Favicon_URL as FIc


#if __name__ == '__main__':
def test_getData():
    f_Icon = FIc.Favicon_URL()
    test_Icon = 'f_icon'
    test_Icons =  ['fav', 'Icon']
    assert(f_Icon.getData(test_Icon) == True)
    assert(f_Icon.getData(test_Icons) == True)
    assert(f_Icon.getData('') == False)
    assert(f_Icon.getData(None) == False)
    return

def test_hasFavicon():
    f_Icon = FIc.Favicon_URL()
    test_Icon = 'f_icon'
    test_Icons =  ['fav', 'Icon']
    assert(f_Icon.hasFavicon(test_Icon) == True)
    assert(f_Icon.hasFavicon(test_Icons) == True)
    assert(f_Icon.hasFavicon('') == False)
    assert(f_Icon.hasFavicon(None) == False)
    return