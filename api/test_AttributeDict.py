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
    u_obj1.makeDict()

    a_dict1 = {
                1:  0,
                2:  0,
                3:  0,
                4:  0,
                5:  0,
                6:  0,
                7:  0,
            }
    
    print("obj1:", u_obj1.getDict())
    print("dict1:", a_dict1)
    
    assert(u_obj1.getDict() == a_dict1)

    u_obj2 = URL_Object() 
    u_obj2.o_URLFavIcon = 0
    u_obj2.o_URLSecureProtocol = 0
    u_obj2.o_CheckProtocol = 0
    u_obj2.o_URLSiteAge = 0
    u_obj2.o_URLLength = 2
    u_obj2.o_SpecialChar = 4
    u_obj2.o_CertificateValid = 0
    u_obj2.makeDict()
    
    a_dict2 = {
                1:  1,
                2:  1,
                3:  1,
                4:  1,
                5:  2,
                6:  4,
                7:  1,
            }
    
    print("obj2:", u_obj2.getDict())
    print("dict2:", a_dict2)
    
    assert(u_obj2.getDict() == a_dict2)

    return

