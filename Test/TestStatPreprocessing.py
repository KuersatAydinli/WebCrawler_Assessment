import unittest
import os, os.path
from Src.StatPDFPreProcessing import StatPDFPreProcessing

class TestStatPreprocessing(unittest.TestCase):
    def test_paper_1(self):
        Dir = 'F:/Wifo_5_Semester/CrowdSourcing/WebCrawler_Assessment/Test/paper1.txt'
        statPreProcessor = StatPDFPreProcessing()
        stat_methods = statPreProcessor.get_method_names()
        method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(Dir,stat_methods)
        print method_bool_dict

