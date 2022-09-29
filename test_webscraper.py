import webscraper as webs
import re

#if __name__ == "__main__":
def test_SetURL():
    ws = webs.Webscraper()
    testURL = "https://python.org/"
    assert(ws.setURL(testURL))
    assert(ws.url == testURL)
    return

def test_GetURL():
    testURL = "https://python.org/"
    ws = webs.Webscraper(testURL)
    assert (ws.getURL() == testURL)
    return

def test_ExistFavicon():
    # rel="icon"
    ws = webs.Webscraper("https://python.org/")
    assert (ws.isExistFavicon() == True)

    # rel="shortcut icon"
    ws.setURL("https://stackoverflow.com/questions/61274239/pythons-regex-or-operator")
    assert (ws.isExistFavicon() == True)

    # no icon
    ws.setURL("https://www.garykessler.net/library/file_sigs.html")
    assert (ws.isExistFavicon() == False)

    return 

def test_extractFavicon():
    ws = webs.Webscraper("https://python.org/")
    assert(re.match(re.compile(".*.ico$"), ws.extractFavicon()[0]))
    ws.setURL("https://stackoverflow.com/questions/61274239/pythons-regex-or-operator")
    assert(re.match(".*.ico$", ws.extractFavicon()[0]))
    ws.setURL("https://www.garykessler.net/library/file_sigs.html")
    assert(re.match("", ws.extractFavicon()[0]))
    return
