import unittest
import os, os.path
from Src.StatPDFPreProcessing import StatPDFPreProcessing

class TestStatPreprocessing(unittest.TestCase):
    def test_paper_1(self):
        paper_one = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Test/FakeStatMethods/paper1.txt'
        statPreProcessor = StatPDFPreProcessing()
        stat_methods = statPreProcessor.get_method_names()
        method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(paper_one,stat_methods)
        count = 0
        for value in method_bool_dict.values():
            if value:
                count +=1
        self.assertEqual(count, 7)

    def test_paper_2(self):
        paper_one = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Test/FakeStatMethods/paper2.txt'
        statPreProcessor = StatPDFPreProcessing()
        stat_methods = statPreProcessor.get_method_names()
        method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(paper_one,stat_methods)
        count = 0
        for value in method_bool_dict.values():
            if value:
                count +=1
        self.assertEqual(count, 8)

    def test_paper_3(self):
        paper_one = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Test/FakeStatMethods/paper3.txt'
        statPreProcessor = StatPDFPreProcessing()
        stat_methods = statPreProcessor.get_method_names()
        method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(paper_one,stat_methods)
        count = 0
        print method_bool_dict
        for value in method_bool_dict.values():
            if value:
                count +=1
        self.assertEqual(count, 6)

