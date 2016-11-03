import unittest
import os, os.path

# Testclass for testing number of PDFs
class TestCrawlerJournalOfManagement(unittest.TestCase):
    def testJanuary(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/January/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 11)

    def testFebruary(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/February/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 11)

    def testMarch(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/March/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 11)

    def testMay(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/May/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 8)

    def testJuly(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/July/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 10)

    def testSeptember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/September/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 12)

    def testNovember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Journal of Management/November/'
        self.assertEqual(len([name for name in os.listdir(Dir)]), 9)
