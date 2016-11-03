# coding=utf-8
import urllib2
import webbrowser

import mechanize as mechanize
import pdfkit
import httplib2
import lxml.html
from lxml import etree
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup
import requests
import urllib
from io import StringIO, BytesIO
import cookielib
import wkhtmltopdf


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
        # response = self.opener.open(download_url).read()
        req = urllib2.Request(download_url,
                              headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib2.urlopen(req).read()
        file = open(path, 'wb')
        file.write(response)
        file.close()
        print("Download Complete for " + str(download_url))

    def get_pdf_links(self):
        links_per_month = {}
        for url in self.base_urls.values():
            pdf_links = lxml.html.fromstring(self.opener.open(url).read()).xpath("//a[contains(@href,'pdfplus')]/@href")
            # response = self.opener.open('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061').read()
            # file = open('out.pdf', 'wb')
            # file.write(response)
            # file.close()
            correct_pdf_links = []
            for pdf_link in pdf_links:
                link = 'http://www.journals.uchicago.edu' + pdf_link
                correct_pdf_links.append(link)

            for month, link in self.base_urls.iteritems():
                if (link == url):
                    links_per_month[month] = correct_pdf_links
        return links_per_month


# sample_url = 'http://www.journals.uchicago.edu/toc/ajs/2014/119/4'
# links = lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read()).xpath(
#     '//a/@href')
# print links
# print lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read())
# print urllib2.urlopen(sample_url).read()


print '====================='
#
# content = urllib2.urlopen(sample_url).read()
# docum = lxml.html.fromstring(content)
# docum.make_links_absolute(sample_url)
# print lxml.html.html_to_xhtml(docum)
#
# soup2 = BeautifulSoup(urllib2.urlopen(sample_url).read())

myclass = ScrapeJournalOfSociology()
# allinks = myclass.get_pdf_links()
# print 'allinks'
# print allinks
# for month,links in allinks.iteritems():
#     print 'month: ' + str(month)
#     print 'len: ' + str(len(links))
#     print '======'

# myclass.download_file('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061',
#                       'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/American Journal of Sociology/January/Doc1.pdf')
sample_url = 'http://www.journals.uchicago.edu/doi/pdfplus/10.1086/675301'
# req = requests.get("http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061")
# print req
# file = open('F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/American Journal of Sociology/January/Doc1.pdf', 'wb')
# file.write(req.content)
# file.close()

# pdfkit.from_url('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061','out.pdf')

# myclass.download_file("http://www.journals.uchicago.edu/doi/pdfplus/10.1086/675301",
#                       "F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/American Journal of Sociology/January/Doc2.txt")

# myclass.get_pdf_links()

# # Browser
# br = mechanize.Browser()
#
# # Cookie Jar
# cj = cookielib.LWPCookieJar()
# br.set_cookiejar(cj)
#
# # Browser options
# br.set_handle_equiv(True)
# br.set_handle_redirect(True)
# br.set_handle_referer(True)
# br.set_handle_robots(False)
#
# # Follows refresh 0 but not hangs on refresh > 0
# br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
#
# # Want debugging messages?
# # br.set_debug_http(True)
# # br.set_debug_redirects(True)
# # br.set_debug_responses(True)
#
#
# f = br.retrieve(sample_url)
# filenew = open('out.pdf', 'wb')
# filenew.write(f)
# filenew.close()
print 'retrieved'
# webbrowser.open('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061')

jar = cookielib.FileCookieJar("cookies")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

print "Currently have %d cookies" % len(jar)
print "Getting page"
response = opener.open('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061').read()
print '============================================================RESPONSE'
file = open('out2.pdf', 'wb')
file.write(response)
file.close()
print '============================================================RESPONSE'
print '============================================================newlinks'
#newlinks = lxml.html.fromstring(opener.open(sample_url).read()).xpath('//table//a[contains(@prop,'Foo')])
newlinks = lxml.html.fromstring(opener.open(sample_url).read()).xpath("//a[contains(@href,'pdfplus')]/@href")
print newlinks
print len(newlinks)
print '============================================================newlinks'
print "Got page"
print "Currently have %d cookies" % len(jar)
print jar
