import ReportMaker as RM

def test_getData():
    u_obj = RM.URL_Object()
    u_obj.o_URL = 'https://tentamen.bth.se/my-exams'
    u_obj.o_URLLength = False
    u_obj.o_URLFavIcon = True
    u_obj.o_URLSecureProtocol = True
    u_obj.o_URLSiteAge = True
    u_obj.o_isSafe = True
    u_obj.o_URLip = '192.169.1.1'
    r_mkr = RM.ReportMaker()
    
    assert(r_mkr.getData(u_obj))
    assert(r_mkr.r_URLO == u_obj)
    return

def test_makeReport():
    u_obj = RM.URL_Object()
    u_obj.o_URL = 'https://tentamen.bth.se/my-exams'
    u_obj.o_URLLength = False
    u_obj.o_URLFavIcon = True
    u_obj.o_URLSecureProtocol = True
    u_obj.o_URLSiteAge = True
    u_obj.o_isSafe = True
    u_obj.o_URLip = '192.169.1.1'
    r_mkr = RM.ReportMaker()
    r_mkr.getData(u_obj)
    r_dic = {
            '1' : u_obj.getURLLength(),
            '2' : u_obj.getURLFavIcon(),
            '3' : u_obj.getURLSecureProtocol(),
            '4' : u_obj.getURLSiteAge(),
            '5' : u_obj.getSafe()
            }
    
    assert(r_mkr.makeReport() == r_dic)

    r_dic = {
            '1' : 0,
            '2' : 1,
            '3' : 1,
            '4' : 1,
            '5' : 1
            }

    assert(r_mkr.makeReport() == r_dic)

    return