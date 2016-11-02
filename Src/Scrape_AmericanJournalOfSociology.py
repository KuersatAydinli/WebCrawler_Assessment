# coding=utf-8
import urllib2
import httplib2
import lxml.html
from lxml import etree
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import requests
import urllib
from io import StringIO, BytesIO
import cookielib


class ScrapeJournalOfSociology():
    base_urls = {'January': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/4',
                 'March': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/5',
                 'May': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/6',
                 'July': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/1',
                 'September': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/2',
                 'November': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/3'}
    jar = cookielib.FileCookieJar("cookies")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

    def download_file(self, download_url, path):
        """

        :param download_url: URL from where to download the content
        :param path: PATH for saving document
        """
        response = self.opener.open(download_url).read()
        file = open(path, 'wb')
        file.write(response)
        file.close()
        print("Download Complete for " + str(download_url))

    def get_pdf_links(self):
        links_per_month = {}
        for url in self.base_urls.values():
            pdf_links = lxml.html.fromstring(self.opener.open(url).read()).xpath("//a[contains(@href,'pdfplus')]/@href")
            correct_pdf_links = []
            for pdf_link in pdf_links:
                link = 'http://www.journals.uchicago.edu' + pdf_link
                correct_pdf_links.append(link)

            for month, link in self.base_urls.iteritems():
                if (link == url):
                    links_per_month[month] = correct_pdf_links
        return links_per_month


sample_url = 'http://www.journals.uchicago.edu/toc/ajs/2014/119/4'
links = lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read()).xpath(
    '//a/@href')
print links
# print lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read())
# print urllib2.urlopen(sample_url).read()


print '====================='

content = urllib2.urlopen(sample_url).read()
docum = lxml.html.fromstring(content)
docum.make_links_absolute(sample_url)
print lxml.html.html_to_xhtml(docum)

soup2 = BeautifulSoup(urllib2.urlopen(sample_url).read())

myclass = ScrapeJournalOfSociology()
# myclass.download_file('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061',
#                       'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/American Journal of Sociology/January/Doc1.pdf')

urllib.urlretrieve("http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061",
                   "F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/American Journal of Sociology/January/Doc1.pdf")
print 'retrieved'

# jar = cookielib.FileCookieJar("cookies")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
#
# print "Currently have %d cookies" % len(jar)
# print "Getting page"
# response = opener.open(sample_url).read()
# print '============================================================RESPONSE'
# #print response
# print '============================================================RESPONSE'
# print '============================================================newlinks'
# #newlinks = lxml.html.fromstring(opener.open(sample_url).read()).xpath('//table//a[contains(@prop,'Foo')])
# newlinks = lxml.html.fromstring(opener.open(sample_url).read()).xpath("//a[contains(@href,'pdfplus')]/@href")
# print newlinks
# print len(newlinks)
# print '============================================================newlinks'
# print "Got page"
# print "Currently have %d cookies" % len(jar)
# print jar
