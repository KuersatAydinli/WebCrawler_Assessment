# -*- coding: utf-8 -*-
import os
from textract import process
from astropy.table import Table, Column
import numpy as np
from astropy.io import ascii
import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import string

data_rows = [(1, 2.0, 'x'),
             (4, 5.0, 'y'),
             (5, 8.2, 'z')]
t = Table(rows=data_rows, names=('a', 'b', 'c'))
print(t)


class StatPDFPreProcessing:
    rootdir = 'F:/Dropbox/Dropbox/all papers'
    stat_method = 'methodlist_full.csv'

    def create_method_bool_dict(self, pdf_path, methods):
        """

        :rtype: dict : dictionnaire with statistical method as key and boolean for occuring in paper as value
        :param pdf_path: path to paper
        :param methods: list of statistical methods specified in 'methodlist_full.csv'
        """
        method_synon_dict = self.create_stat_method_dict()  # Key: stat. method - Value: list of acronyms, synonyms

        method_bool_mapping = {}
        for method in methods:
            method_bool_mapping[method] = False  # Initialize all values to False for all stat. methods

        pdf_text = process(pdf_path, language='eng')
        for key, values in method_synon_dict.iteritems():
            if len(values) >= 1:
                for value in values:
                    if pdf_text.lower().translate(None, string.punctuation).find(
                            value[1:].lower().translate(None, string.punctuation)) != -1:
                        method_bool_mapping[key] = True
            if pdf_text.lower().translate(None, string.punctuation).find(
                    key.lower().translate(None, string.punctuation)) != -1:
                method_bool_mapping[key] = True
        return method_bool_mapping

    def create_initial_table(self):
        """
        Create initial empty Table for final analysis
        """
        method_names = self.get_method_names()
        table = Table()
        method_column = Column(name='stat. Methods', data=method_names)
        table.add_column(method_column)
        # journal_names = os.listdir(self.rootdir)
        # journal_columns = []
        # strs = ["" for x in range(31)] # empty string as default entry for table cell
        # for journal in journal_names:
        #     journal_column = Column(name=journal, data=strs)
        #     journal_columns.append(journal_column)
        # table.add_columns(journal_columns)
        # print ascii.write(table, format='fixed_width')
        return table

    def get_method_names(self):
        """
        Create list of statistical method identifiers
        """
        method_names = []
        with open(self.stat_method, 'r') as method_file:
            for line in method_file.readlines():
                method_names.append(line.split(',')[0])
        return method_names

    def create_stat_method_dict(self):
        """
        Create dict of statistical method and its synonyms
        """
        with open(self.stat_method, 'r') as file:
            stat_method_dict = {}
            for line in file.readlines():
                stat_method_dict[line.split(',')[0]] = line.split(',')[1:]
        return stat_method_dict


statPreProcessor = StatPDFPreProcessing()
stat_table = statPreProcessor.create_initial_table()
method_dict = statPreProcessor.create_stat_method_dict()
stat_methods = statPreProcessor.get_method_names()
print stat_methods

# Testing Management of Science statistics

testDir = 'F:/Dropbox/Dropbox/all papers/Management of Science'
count = 1
method_bool_dicts = [{}]
method_count_dict = {}  # count in how many papers a stat. method appears: Key: method - Value: #Papers
for method in stat_methods:
    method_count_dict[method] = 0

for month_issue in os.listdir(testDir):
    for file in os.listdir(testDir + '/' + month_issue):
        # print (file,count)
        count += 1
        method_bool_dict = statPreProcessor.create_method_bool_dict(testDir + "/" + month_issue + "/" + file,
                                                                    stat_methods)
        for method, occ in method_bool_dict.iteritems():
            if occ == True:
                method_count_dict[method] += 1
        print ('Month: ' + month_issue, 'File: ' + file, method_bool_dict)

print method_count_dict
testString = 'Mantel – Haenszel'
print testString.translate(None, string.whitespace)

method_occurences = list(method_count_dict.values())
stat_column = Column(name='Management of Science', data=method_occurences)
stat_table.add_column(stat_column)
print ascii.write(stat_table, format='fixed_width')
# text = process('F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs/Management of Science/June/Doc8.pdf', language='eng')
# print 't-test' in text
# print statPreProcessor.create_method_bool_dict('F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs/Management of Science/June/Doc8.pdf',stat_methods)

# stat_method_dict = {}
# with open('methodlist_full.csv', 'r') as file:
#     for line in file.readlines():
#         stat_method_dict[line.split(',')[0]] = line.split(',')[1:]
#     print stat_method_dict

# #rootdir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs'

# print os.listdir(rootdir)
#
# Add the three Journals also to all papers directory
# rootdir = 'F:/Dropbox/Dropbox/all papers'
# count = 1
# for subdir, dirs, files in os.walk(rootdir):
#     for file in files:
#         print (os.path.join(subdir, file),count)
#         count+=1

# WORKS THE BEST
# from textract import process
# text = process('F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs/Management of Science/June/Doc14.pdf', language='eng')
# print '' in text

# with open('methodlist_full.csv', 'r') as file:
#     methods = []
#     for line in file.readlines():
#         for method in line.split(','):
#             methods.append(method)
# print methods
#
# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = file(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
#
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)
#
#     text = retstr.getvalue()
#
#     fp.close()
#     device.close()
#     retstr.close()
#     return text
#
# print convert_pdf_to_txt('F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs/Management of Science/June/Doc14.pdf')
