#encoding=utf-8
__author__ = 'Richard'

import urllib2
import re
import os
#
def getContent(url):
    request = urllib2.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6')
    opener = urllib2.build_opener()
    f= opener.open(request)
    content = f.read().decode('GB18030','ignore')
    return content

def buildPageUrl(startUrl):
    pre = startUrl[0:32]
    post = startUrl[33:len(startUrl)]
    for i in range(2,8):
        url = pre + '/page/' + str(i) +'?'+ post
        print url

def getArticleUrl(content):
    articleExp = r'<a\sclass=\"title\"\shref=.*?>'
    articleReg = re.compile(articleExp)
    articleUrlList = re.findall(articleExp,content)
    articleList = []
    for articleUrl in articleUrlList:
        articleUrl = "http://link.springer.com/" + articleUrl[24:len(articleUrl)-2]
        print articleUrl
        articleList.append(articleUrl)
    return articleList

def buildCitationUrls(articleUrlList):
    citationList = []
    for url in articleUrlList:
        url = "http://link.springer.com/export-citation" + url[24:len(url)] + '.bib'
        citationList.append(url)
        print url
    return citationList

def buildCitationUrl(url):
    citationUrl = "http://link.springer.com/export-citation" + url[24:len(url)] + '.bib'
    print citationUrl
    return  citationUrl

def getAbstract(url):
    content = getContent(url)
    #print content
    abstractExp = r'Para\">[\s\S]*?</p>'
    abstractReg = re.compile(abstractExp)
    abstractList = re.findall(abstractReg,content)
    abstract = abstractList[0]
    abstract = abstract[6:len(abstract)-4]
    return abstract
    #print abstract

def getBib(url,abstract):
    content = getContent(url)
    #print abstract
    content = content[0:len(content)-2]+',' + 'abstract={'+abstract+'}\n'+'}'
    n = content.index('year')
    m = content.index('volume')
    year = content[16:20]
    volume = content[m+8:m+11]
    info = {}
    info["year"] = year
    info["volume"] = volume
    info["citation"] = content
    return info

def buildCitation(url):
    citationUrl = buildCitationUrl(url)
    abstract = getAbstract(url)

    #print abstract
    bib = getBib(citationUrl,abstract)
    print bib['year']
    print bib['volume']
    print bib['citation']
    writeCitation(bib)

def writeCitation(citation):
    path = 'G:\\IJCV\\' + citation['year']
    print path
    print os.path.exists(path)
    citationFile = open('G:\\citation.txt','a')
    citationFile.write(unicode.encode(citation,'utf-8'))
    citationFile.write('\n')

startUrl = 'http://link.springer.com/search?sortOrder=newestFirst&facet-content-type=Article&facet-journal-id=11263'
url = "http://link.springer.com/search?sortOrder=newestFirst&facet-content-type=Article&facet-journal-id=11263"

#content = getContent(url)
#articleList = getArticleUrl(content)

abstractUrl = 'http://link.springer.com/export-citation/article/10.1007/s11263-014-0742-4.bib'
articleUrl = 'http://link.springer.com/article/10.1007/s11263-015-0809-x'
#buildCitationUrl(articleUrl)
buildCitation(articleUrl)
#getBib(abstractUrl)
#getAbstract(articleUrl)
#buildCitationUrl(articleList[0])
#buildCitationUrls(articleList)
#buildPageUrl(startUrl)
