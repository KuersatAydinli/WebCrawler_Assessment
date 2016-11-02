# coding=utf-8
import urllib2

import lxml.html


class ScrapeJournalOfSociology():
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

