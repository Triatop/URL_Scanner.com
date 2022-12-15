from URL_Object import URL_Object


def test_attributeDict():
    u_obj1 = URL_Object()
    u_obj1.o_URLFavIcon = 1
    u_obj1.o_URLSecureProtocol = 1
    u_obj1.o_CheckProtocol = 1
    u_obj1.o_URLSiteAge = 1
    u_obj1.o_URLLength = 0
    u_obj1.o_SpecialChar = 0
    u_obj1.o_CertificateValid = 1
    u_obj1.o_URLLinks = 0
    u_obj1.makeDict()

    a_dict1 = {
        1:  0,
        2:  0,
        3:  0,
        4:  0,
        5:  0,
        6:  0,
        7:  0,
        8:  0,
        9:  0,
        10: 0,
        11: 0,
    }

    print("obj1:", u_obj1.getDict())
    print("dict1:", a_dict1)

    assert (u_obj1.getDict() == a_dict1)

    u_obj1.setURLFavIcon(0)
    u_obj1.setURLSecureProtocol(0)
    u_obj1.setCheckPort(0)
    u_obj1.setURLSiteAge(0)
    u_obj1.setURLLength(2)
    u_obj1.setSpecialCharater(4)
    u_obj1.setCertificateValid(0)
    u_obj1.setURLLinks(9)
    u_obj1.setIsCharSwapped(1)
    u_obj1.setPulseCount(23)
    u_obj1.setMalFileCount(63)
    u_obj1.makeDict()

    a_dict1 = {
        1:  1,
        2:  1,
        3:  1,
        4:  1,
        5:  2,
        6:  4,
        7:  1,
        8:  9,
        9:  1,
        10: 23,
        11: 63
    }

    assert (u_obj1.getDict() == a_dict1)

    return
