import unittest
import os, os.path
from Src.StatPDFPreProcessing import StatPDFPreProcessing

class TestStatPreprocessing(unittest.TestCase):
    def test_paper_1(self):
        paper_one = 'paper1.txt'
        statPreProcessor = StatPDFPreProcessing()
        stat_methods = statPreProcessor.get_method_names()
        method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(paper_one,stat_methods)
        print method_bool_dict

