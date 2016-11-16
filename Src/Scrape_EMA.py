import cookielib
import urllib2
from lxml.html import parse
import lxml.html
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html

class Scrape_EMA():
    base_urls = {'Kyprolis': 'https://clinicaldata.ema.europa.eu/web/cdp/search?p_p_id=cdpdossierviewportlet_WAR_cdpdossierviewportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&folderName=EMEAHC0037900000',
                 'Zurampic': 'https://clinicaldata.ema.europa.eu/web/cdp/search?p_p_id=cdpdossierviewportlet_WAR_cdpdossierviewportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&folderName=EMEAHC0039320000'}

    jar = cookielib.FileCookieJar("cookies")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

    def download_file(self, download_url, path):
        """

        :param download_url: URL from where to download the content
        :param path: PATH for saving document
        """
        # response = self.opener.open(download_url).read()
        jar = cookielib.FileCookieJar("cookies")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        response = opener.open(download_url).read()
        file = open(path, 'wb')
        file.write(response)
        file.close()
        print("Download Complete for " + str(download_url))

    def get_pdf_links(self):
        links_per_name = {}
        for url in self.base_urls.values():
            # pdf_links = lxml.html.fromstring(self.opener.open(url).read()).xpath("//a[contains(text(),'m53')]/@href")
            # pdf_links = lxml.html.fromstring(self.opener.open(url).read()).xpath("//a")
            pdf_links = lxml.html.fromstring(self.opener.open(url).read()).xpath("//a/@href")
            dom = parse(url).getroot()
            links = dom.cssselect('a')
            print 'parse length: ' + str(len(links))
            # correct_pdf_links = []
            # for pdf_link in pdf_links:
            #     link = 'http://www.journals.uchicago.edu' + pdf_link
            #     correct_pdf_links.append(link)

            for name, link in self.base_urls.iteritems():
                if (link == url):
                    links_per_name[name] = pdf_links
            for key,value in links_per_name.iteritems():
                print (key, value)
        return links_per_name

# emaScrape = Scrape_EMA()
# print emaScrape.get_pdf_links()

class Render(QWebpage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        r.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

url = 'http://pycoders.com/archive/'
#This does the magic.Loads everything
r = Render(url)
#result is a QString.
result = r.frame.toHtml()

#QString should be converted to string before processed by lxml
formatted_result = str(result.toAscii())

#Next build lxml tree from formatted_result
tree = html.fromstring(formatted_result)

#Now using correct Xpath we are fetching URL of archives
archive_links = tree.xpath('//divass="campaign"]/a/@href')
print archive_links

from StringIO import StringIO
from lxml import etree
test_link = 'https://clinicaldata.ema.europa.eu/web/cdp/search?p_p_id=cdpdossierviewportlet_WAR_cdpdossierviewportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&folderName=EMEAHC0037900000'
# ufile = urllib2.urlopen("https://clinicaldata.ema.europa.eu/web/cdp/search?p_p_id=cdpdossierviewportlet_WAR_cdpdossierviewportlet&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&folderName=EMEAHC0037900000")
#
# root = etree.parse(ufile, etree.HTMLParser())

# print etree.tostring(root)
# driver = webdriver.Firefox()
# driver.get(test_link)
# htmlSource = driver.page_source
# print htmlSource


