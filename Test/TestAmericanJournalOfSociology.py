import unittest
import os, os.path


# Testclass for testing number of PDFs
class TestCrawlerJournalOfManagement(unittest.TestCase):
    def testJanuary(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/January/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 32)

    def testMarch(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/March/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 36)

    def testMay(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/May/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 40)

    def testJuly(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/July/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 29)

    def testSeptember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/September/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 29)

    def testNovember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/American Journal of Sociology/November/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 30)
