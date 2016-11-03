# coding=utf-8
import cookielib
import urllib2
import lxml.html


class ScrapeMangementOfScience:
    base_urls = {'January': 'http://pubsonline.informs.org/toc/mnsc/60/1',
                 'February': 'http://pubsonline.informs.org/toc/mnsc/60/2',
                 'March': 'http://pubsonline.informs.org/toc/mnsc/60/3',
                 'April': 'http://pubsonline.informs.org/toc/mnsc/60/4',
                 'May': 'http://pubsonline.informs.org/toc/mnsc/60/5',
                 'June': 'http://pubsonline.informs.org/toc/mnsc/60/6',
                 'July': 'http://pubsonline.informs.org/toc/mnsc/60/7',
                 'August': 'http://pubsonline.informs.org/toc/mnsc/60/8',
                 'September': 'http://pubsonline.informs.org/toc/mnsc/60/9',
                 'October': 'http://pubsonline.informs.org/toc/mnsc/60/10',
                 'November': 'http://pubsonline.informs.org/toc/mnsc/60/11',
                 'December': 'http://pubsonline.informs.org/toc/mnsc/60/12'}
    jar = cookielib.FileCookieJar("cookies")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

    def download_file(self, download_url, path):
        """

        :param download_url: URL from where to download the content
        :param path: PATH for saving document
        """
        # response = self.opener.open(download_url).read()
        jar = cookielib.FileCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
        response = opener.open(download_url).read()
        file = open(path, 'wb')
        file.write(response)
        file.close()
        print("Download Complete for " + str(download_url))

    def get_pdf_links(self):
        links_per_month = {}
        for url in self.base_urls.values():
            hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'User-Agent': 'Mozilla/5.0'}
            req = urllib2.Request(url, headers=hdr)
            page = urllib2.urlopen(req)
            # pdf_links = lxml.html.fromstring(opener.open(url).read()).xpath("//a[contains(@href,'/doi/pdf')]/@href")
            pdf_links = lxml.html.fromstring(page.read()).xpath("//a[contains(@href,'/doi/pdf')]/@href")
            correct_pdf_links = []
            for pdf_link in pdf_links:
                link = 'http://pubsonline.informs.org' + pdf_link
                correct_pdf_links.append(link)

            for month, link in self.base_urls.iteritems():
                if (link == url):
                    links_per_month[month] = correct_pdf_links
        return links_per_month

# jar = cookielib.FileCookieJar("cookies")
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
# pdf_links = lxml.html.fromstring(opener.open('http://pubsonline.informs.org/toc/mnsc/60/1').read()).xpath(
#     "//a[contains(@href,'/doi/pdf')]/@href")
# print pdf_links
# print len(pdf_links)

crawlerManagementOfScience = ScrapeMangementOfScience()
allLinks_ManagementOfScience = crawlerManagementOfScience.get_pdf_links()

for month, links in allLinks_ManagementOfScience.iteritems():
    if month == 'August':
        counter = 1
        for link in links:
            crawlerManagementOfScience.download_file(link,
                                            "F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/"
                                            + month + '/Doc' + str(counter) + '.pdf')
            counter += 1
        print 'DOWNLOAD COMPLETED FOR ' + str(month).upper()
        exit()

# site = 'http://pubsonline.informs.org/toc/mnsc/60/8'
# hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
# req = urllib2.Request(site, headers=hdr)
# try:
#     page = urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.fp.read()
#
# content = page.read()
# print content