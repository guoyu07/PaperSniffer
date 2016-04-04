import os
import urllib2
def getFilenames(fileDir):
    pass

def getBibtex(queryWords):
    pass

def getScholarResults(queryWords):
    url = 'https://www.google.com.sg/webhp?hl=en#hl=en&q=' + queryWords
    print url
    proxy = urllib2.ProxyHandler({'https':'http://127.0.0.1:16823/'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url)
    html = response.read()
    print html


if __name__ == "__main__":
    getScholarResults("Superpixel")
