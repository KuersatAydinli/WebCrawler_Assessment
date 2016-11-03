# coding=utf-8
import urllib2

import lxml.html


class ScrapeJournalOfManagement():
    def __init__(self):
        pass

    base_urls = {'January': 'http://jom.sagepub.com/content/40/1.toc',
                 'February': 'http://jom.sagepub.com/content/40/2.toc',
                 'March': 'http://jom.sagepub.com/content/40/3.toc',
                 'May': 'http://jom.sagepub.com/content/40/4.toc',
                 'July': 'http://jom.sagepub.com/content/40/5.toc',
                 'September': 'http://jom.sagepub.com/content/40/6.toc',
                 'November': 'http://jom.sagepub.com/content/40/7.toc'}

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

    def get_pdf_links(self):
        """

        :return: Dictionary with the month´s as keys and all the pdf links from that month as values
        """
        links_per_month = {}
        for url in self.base_urls.values():
            # Get all links of a url
            links = lxml.html.fromstring(urllib2.urlopen(url).read()).xpath('//a/@href')
            pdf_links = []

            # Extract PDF links
            for link in links:
                if 'full.pdf' in link:
                    pdf_links.append(link)
            correct_pdf_links = []

            # Adjust pdf links
            for pdf_link in pdf_links:
                link = 'http://jom.sagepub.com' + pdf_link[:-5]
                correct_pdf_links.append(link)

            # for each month as key add list of all pdf links as corresponding value
            for month, link in self.base_urls.iteritems():
                if (link == url):
                    links_per_month[month] = correct_pdf_links
        return links_per_month


# Download all PDFs of Journal of Management
basicCrawler = ScrapeJournalOfManagement()
all_links_JournalOfManagement = basicCrawler.get_pdf_links()
# Iterate through each month and download all PDF links from that month
for month, links in all_links_JournalOfManagement.iteritems():
    counter = 1
    for link in links:
        basicCrawler.download_file(link, 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/'
                                   + month + '/Doc' + str(counter) + '.pdf')
        counter += 1
    print 'DOWNLOAD COMPLETED FOR ' + str(month).upper()

# print all_links_JournalOfManagement


# //div/descendant::h4[@class="cit-title-group" and /descendant::a[@href="/content/40/2/353.full.pdf+html"]]
# XPATH: /html[1]/body[1]/div[1]/div[8]/form[1]/div[.//h4[@class="cit-title-group"] and .//a[@href="/content/40/2/353.full.pdf+html"]]//h4/text()[1]
# for month, links in basicCrawler.get_pdf_links().iteritems():
#     if month == 'February':
#         print 'Names for February: '
#         link_name_dictionnaire = {}
#         baselink = basicCrawler.base_urls.get(month)
#         print baselink
#         content = lxml.html.fromstring(urllib2.urlopen(baselink).read())
#         # print lxml.html.fromstring(urllib2.urlopen(link).read()).text()
#         for link in links:
#             correctLink = link[22:] + '+html'
#             primaryName = content.xpath("//div/descendant::h4[@class='cit-title-group' and /descendant::a[@href='"
#                     + str(correctLink) + "']]/text()")
#             link_name_dictionnaire[link] = primaryName
#             print link_name_dictionnaire
#         exit()
