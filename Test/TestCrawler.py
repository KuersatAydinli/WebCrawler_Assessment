import unittest
import os, os.path



class TestCrawlerJournalOfManagement(unittest.TestCase):
    def testJanuary(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/January/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),11)

    def testFebruary(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/February/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),11)

    def testMarch(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/March/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),11)

    def testMay(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/May/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),8)

    def testJuly(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/July/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),10)

    def testSeptember(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/September/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),12)

    def testNovember(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Src/Journal of Management/September/'
        self.assertEqual(len([name for name in os.listdir(Dir)]),9)

