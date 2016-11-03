# coding=utf-8
import cookielib
import urllib2

import lxml.html


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
        jar = cookielib.FileCookieJar("cookies")
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        response = opener.open(download_url).read()
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

crawlerJournalSoc = ScrapeJournalOfSociology()
allLinks_JournalOfSociology = crawlerJournalSoc.get_pdf_links()
for month, links in allLinks_JournalOfSociology.iteritems():
    if month == 'January':
        counter = 1
        for link in links:
            crawlerJournalSoc.download_file(link,
                                            "F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/"
                                            + month + '/Doc' + str(counter) + '.pdf')
            counter += 1
        print 'DOWNLOAD COMPLETED FOR ' + str(month).upper()


# Sample Use of CookieJar for using urllib2

# jar = cookielib.FileCookieJar("cookies")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
#
# print "Currently have %d cookies" % len(jar)
# print "Getting page"
# response = opener.open('http://www.journals.uchicago.edu/doi/pdfplus/10.1086/677061').read()
# print '============================================================RESPONSE'
# print response
# print '============================================================RESPONSE'
# print '============================================================PDF Links'
# pdf_links = lxml.html.fromstring(opener.open(sample_url).read()).xpath("//a[contains(@href,'pdfplus')]/@href")
# print pdf_links
# print len(pdf_links)
# print '============================================================PDF Links'
# print "Got page"
# print "Currently have %d cookies" % len(jar)
# print jar
