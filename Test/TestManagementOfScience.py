import unittest
import os, os.path

class TestManagementOfScience(unittest.TestCase):
    def testJanuary(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/January/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 15)

    def testFebruary(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/February/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 18)

    def testMarch(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/March/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 16)

    def testApril(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/April/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 16)

    def testMay(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/May/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 17)

    def testJune(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/June/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 15)

    def testJuly(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/July/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 14)

    def testAugust(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/August/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 14)

    def testSeptember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/September/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 15)

    def testOctober(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/October/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 14)

    def testNovember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/November/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 14)

    def testDecember(self):
        Dir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment/Management of Science/December/'
        self.assertEqual(len([name for name in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, name))]), 14)
