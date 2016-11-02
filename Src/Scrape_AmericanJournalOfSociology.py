# coding=utf-8
import urllib2
import httplib2
import lxml.html
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup as bs
import requests

class ScrapeJournalOfSociology():
    base_urls = {'January': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/4',
                 'March': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/5',
                 'May': 'http://www.journals.uchicago.edu/toc/ajs/2014/119/6',
                 'July': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/1',
                 'September': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/2',
                 'November': 'http://www.journals.uchicago.edu/toc/ajs/2014/120/3'}

    def download_file(self, download_url, path):
        """

        :param download_url: URL from where to download the content
        :param path: PATH for saving document
        """
        response = urllib2.urlopen(download_url)
        file = open(path, 'wb')
        file.write(response.read())
        file.close()
        print("Download Complete for " + str(download_url))


sample_url = 'http://www.journals.uchicago.edu/toc/ajs/2014/119/4'
links = lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read()).xpath('//a/@href')
print links
#print lxml.html.fromstring(urllib2.urlopen('http://www.journals.uchicago.edu/toc/ajs/2014/119/4').read())
#print urllib2.urlopen(sample_url).read()

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print "Encountered a start tag:", tag
#
#     def handle_endtag(self, tag):
#         print "Encountered an end tag :", tag
#
#     def handle_data(self, data):
#         print "Encountered some data  :", data
#
# parser = MyHTMLParser()
# parser.feed(urllib2.urlopen(sample_url).read())

# http = httplib2.Http()
# status, response = http.request(sample_url)
#
# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print link['href']

# connection = urllib2.urlopen(sample_url)
#
# dom =  lxml.html.fromstring(connection.read())
#
# for link in dom.xpath('//@href'): # select the url in href for all a tags(links)
#     print link

request = urllib2.Request(sample_url)
response = urllib2.urlopen(request)
html = urllib2.urlopen(sample_url).read()
soup = bs(html)
linksnew = soup.findAll('a')
for tag in linksnew:
    link = tag.get('href',None)
    if link is not None:
        print link

print '====================='

url = sample_url
tree = lxml.html.parse(url)
#listings = tree.xpath("//a[contains(@href,'/doi/pdfplus')]")
#listings = tree.xpath("//a[@href='/doi/pdfplus/10.1086/674561']")
listings = tree.xpath("//a/text()")
print listings



