import urllib2
import re
import lxml.html
import urlparse
from lxml import etree
from io import StringIO, BytesIO
from HTMLParser import HTMLParser
from BeautifulSoup import BeautifulSoup as bs


base_url = 'http://jom.sagepub.com/content/40/1.toc?hwshib2=authn%3A1478163376%3A20161102%253A8a26d5df-f892-4fa2-afc6-c4825e150c66%3A0%3A0%3A0%3Ai77sfFF%2FA9DR8Jvym4MjiQ%3D%3D'
res = urllib2.urlopen(base_url).read()
print res
#tree = lxml.html.fromstring(res.read())

ns = {'re': 'http://exslt.org/regular-expressions'}

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("AmericanJournal2.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

def get_title(download_url):
    body = urllib2.urlopen(download_url())
    parsed_html = bs(body)
    print parsed_html.body.find('h4', attrs={'class':'cit-title-group'})




#for node in tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns):
    # print the href, joining it to the base_url
 #   print urlparse.urljoin(base_url, node.attrib['href'])

#parser = etree.HTMLParser()
#treeNew = etree.parse(StringIO(res), parser)
#result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
print 'RESULT'
doc = lxml.html.parse(urllib2.urlopen(base_url))
#print lxml.html.find_rel_links(lxml.html.fromstring(urllib2.urlopen(base_url)),'href')
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

#parser = MyHTMLParser()
#parser.feed(res)

get_title('http://jom.sagepub.com/content/40/1.toc?hwshib2=authn%3A1478163376%3A20161102%253A8a26d5df-f892-4fa2-afc6-c4825e150c66%3A0%3A0%3A0%3Ai77sfFF%2FA9DR8Jvym4MjiQ%3D%3D')