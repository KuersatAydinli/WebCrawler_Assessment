import urllib2
import re
import lxml.html
import urlparse
from lxml import etree
from io import StringIO, BytesIO
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup as bs
from shutil import copyfile
from pyPdf import PdfFileWriter, PdfFileReader
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


base_url = 'http://jom.sagepub.com/content/40/1.toc?hwshib2=authn%3A1478163376%3A20161102%253A8a26d5df-f892-4fa2-afc6-c4825e150c66%3A0%3A0%3A0%3Ai77sfFF%2FA9DR8Jvym4MjiQ%3D%3D'
res = urllib2.urlopen(base_url).read()
print res
#tree = lxml.html.fromstring(res.read())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

class ScrapeAmericanSocJournal():
    base_urls = {}
    base_urls['January'] = 'http://jom.sagepub.com/content/40/1.toc'
    base_urls['February'] = 'http://jom.sagepub.com/content/40/2.toc'
    base_urls['March'] = 'http://jom.sagepub.com/content/40/3.toc'
    base_urls['May'] = 'http://jom.sagepub.com/content/40/4.toc'
    base_urls['July'] = 'http://jom.sagepub.com/content/40/5.toc'
    base_urls['September'] = 'http://jom.sagepub.com/content/40/6.toc'
    base_urls['November'] = 'http://jom.sagepub.com/content/40/7.toc'

    def download_file(self,download_url,path):
        response = urllib2.urlopen(download_url)
        file = open(path, 'wb')
        file.write(response.read())
        file.close()
        print("Completed")

    def get_pdf_links(self):
        links_per_month = {}
        for url in self.base_urls.values():
            links = lxml.html.fromstring(urllib2.urlopen(url).read()).xpath('//a/@href')
            pdf_links = []
            for link in links:
                if 'full.pdf' in link:
                    pdf_links.append(link)
            correct_pdf_links = []
            for pdf_link in pdf_links:
                link = 'http://jom.sagepub.com'+pdf_link[:-5]
                correct_pdf_links.append(link)

            for month,link in self.base_urls.iteritems():
                if (link==url):
                    links_per_month[month] = correct_pdf_links

def download_file(download_url, path):
    response = urllib2.urlopen(download_url)
    file = open(path, 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

# def get_title(download_url):
#     body = urllib2.urlopen(download_url())
#     parsed_html = bs(body)
#     print parsed_html.body.find('h4', attrs={'class':'cit-title-group'})


print 'RESULT'
doc2 = lxml.html.parse(urllib2.urlopen(base_url))

links = lxml.html.fromstring(urllib2.urlopen(base_url).read()).xpath('//a/@href')
print links
pdf_links = []
for link in links:
    if 'full.pdf' in link:
        pdf_links.append(link)

print pdf_links

correct_pdf_links = []
for pdf_link in pdf_links:
    link = 'http://jom.sagepub.com'+pdf_link[:-5]
    correct_pdf_links.append(link)

print correct_pdf_links

count = 1
for link in correct_pdf_links:
    download_file(link,'Src/Journal of Management/January/Doc'+str(count)+'.pdf')
    count = count+1