#encoding=utf-8
__author__ = 'Richard'
import urllib2

class PaperSnifer():

    def __init__(self, url):
        self.urls = []
        self.pdfurls = []
        self.biburls = []
        self.url = url
        self.papertitles = []

    def getContents(self, url):
        page = urllib2.urlopen(url)
        contents = page.read()
        return contents

    def getInfo(self, contents):

        return
    def downloader(self, pdflinks):
      return 0



