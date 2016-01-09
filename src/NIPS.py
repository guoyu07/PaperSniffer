#encoding=utf-8
__author__ = 'Richard'
import urllib2
from bs4 import BeautifulSoup
import re
import time

class NipsSnifer():

    def __init__(self, url):
        self.urls = []
        self.pdfurls = []
        self.bibs = []
        self.url = url
        self.papertitles = []
        self.contents = ''

    def getContents(self):
        page = urllib2.urlopen(self.url)
        contents = page.read()
        return contents

    def getInfo(self):
        soup = BeautifulSoup(contents)
        # print contents
        print soup.title
        urllist = soup.find_all(href=re.compile("pdf"))
        bibList = soup.find_all("div",{"class": "bibref"})
        print len(bibList)

        for bib in bibList:
            self.bibs.append(bib.get_text())

        for url in urllist:
            url = "http://www.cv-foundation.org/openaccess/" + url['href']
            self.pdfurls.append(url)
        titlelist = soup.find_all("dt")
        for title in titlelist:
            title = title.get_text()
            title = title.replace(u":", " ")
            title = title.replace(u"/", "-")
            title = title.replace(u"%", " ")
            title = title.replace(u"?", " ")
            title = title.replace(u"*", " ")
            self.papertitles.append(title)
            print title
        # print len(urllist)
        print urllist[0]['href']
        # print self.pdfurls
        # print titlelist
        print self.bibs
        return 0

    def writeBibs(self, path='ref.bib'):
        file = open(path,'a')
        for bib in self.bibs:
            file.write(bib.encode('utf-8'))

    def downloader(self):
        for i in range(120,len(self.pdfurls)):
            self.getFile(self.pdfurls[i],self.papertitles[i]+".pdf")
            time.sleep(5)
        return 0

    def getFile(self, url, file_name):
        u = urllib2.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            status = r" %10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,
        f.close()

if __name__ == '__main__':
    print "Success"