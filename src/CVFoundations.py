#encoding=utf-8
__author__ = 'Richard'
import urllib2
from bs4 import BeautifulSoup
import re

class PaperSnifer():

    def __init__(self, url):
        self.urls = []
        self.pdfurls = []
        self.biburls = []
        self.url = url
        self.papertitles = []
        self.contents = ''

    def getContents(self):
        page = urllib2.urlopen(self.url)
        contents = page.read()
        return contents

    def getInfo(self):
        soup = BeautifulSoup(contents)
        print soup.title
        urllist = soup.find_all(href=re.compile("pdf"))
        titleList = soup.find_all('div')
        print urllist
        print titleList

        return 0

    def downloader(self, pdflinks):
      return 0


if __name__ == '__main__':
    paperSnifer = PaperSnifer("http://www.cv-foundation.org/openaccess/ICCV2015.py")
    contents = paperSnifer.getContents()
    paperSnifer.getInfo()

