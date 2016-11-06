# -*- coding: utf-8 -*-
import os

import PyPDF2
from textract import process
from astropy.table import Table, Column
import numpy as np
from astropy.io import ascii
import re
import json
import pickle
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from tika import parser
import string
import tables
from operator import add
import time
import pyPdf


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

        :rtype: dict : dictionary with statistical method as key and boolean for occuring in paper as value
        :param pdf_path: path to paper
        :param methods: list of statistical methods specified in 'methodlist_full.csv'
        """
        method_synon_dict = self.create_stat_method_dict()  # Key: stat. method - Value: list of acronyms, synonyms

        method_bool_mapping = {}
        for method in methods:
            method_bool_mapping[method] = False  # Initialize all values to False for all stat. methods

        try:
            pdf_text = process(pdf_path, language='eng')
        except:
            pdf_text = ''

        for key, values in method_synon_dict.iteritems():
            regex_list = []
            for value in values:
                regex_list.append(value.rstrip().replace("\xe2\x80\x93", "-"))
            regex_list.append(key.rstrip().replace("\xe2\x80\x93", "-"))
            for i, regex in enumerate(regex_list):
                if regex != "" and regex.lower() != "CI".lower():
                    if pdf_text.lower().translate(None, string.punctuation).rstrip().replace("\xe2\x80\x93", "-").find(
                            regex.lower().translate(None, string.punctuation)) != -1:
                        method_bool_mapping[key] = True
                        # if len(values) >= 1:
                        #     for value in values:
                        #         if value != '\\n':
                        #             if pdf_text.lower().translate(None, string.punctuation).find(
                        #                     value.lower().translate(None, string.punctuation)) != -1:
                        #                 method_bool_mapping[key] = True
                        # if pdf_text.lower().translate(None, string.punctuation).find(
                        #         key.lower().translate(None, string.punctuation)) != -1:
                        #     method_bool_mapping[key] = True
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


start_time = time.time()
#
statPreProcessor = StatPDFPreProcessing()
stat_table = statPreProcessor.create_initial_table()
method_dict = statPreProcessor.create_stat_method_dict()
stat_methods = statPreProcessor.get_method_names()
print stat_methods
cleaned = []
for method in stat_methods:
    cleaned.append(method.rstrip().replace("\xe2\x80\x93", "-"))
print len(cleaned)
print 'test string\n'.rstrip()

# Testing Management of Science statistics

# testDir = 'F:/Dropbox/Dropbox/all papers/Management of Science'
# main_dir = 'F:/Dropbox/Dropbox/all papers'
#
# counter = 1
#
# journal_counts = {}
# for journal in os.listdir(main_dir):
#     journal_counts[journal] = sum([len(files) for r, d, files in os.walk(main_dir + "/" + journal)])
# print journal_counts
#
# for journalDirectory in os.listdir(main_dir):
#     method_count_dict = {}  # count in how many papers a stat. method appears: Key: method - Value: #Papers
#     method_percent_dict = {}  # same as method_count_dict - only with percentage values
#     for method in stat_methods:
#         method_count_dict[method.rstrip().replace("\xe2\x80\x93", "-")] = 0
#
#     for month_issue in os.listdir(main_dir + "/" + journalDirectory):
#         for file in os.listdir(main_dir + "/" + journalDirectory + '/' + month_issue):
#             # print (file,count)
#             method_bool_dict = statPreProcessor.create_method_bool_dict(
#                 main_dir + "/" + journalDirectory + "/" + month_issue + "/" + file,
#                 stat_methods)
#             print (journalDirectory, month_issue, file, counter)
#             for method, occ in method_bool_dict.iteritems():
#                 if occ == True:
#                     method_count_dict[method.rstrip().replace("\xe2\x80\x93", "-")] += 1
#             counter += 1
#     # numpy_file = open('method_count_dict.npy', 'a')
#     # try:
#     #     np.savetxt(numpy_file, method_count_dict)
#     # except:
#     #     pass
#     pickle_file = open('method_count_dict.pkl', 'a')
#     try:
#         pickle.dump(pickle_file,method_count_dict)
#     except:
#         pass
#     json_file = open('method_count_dict.txt', 'a')
#     try:
#         json.dump(method_count_dict,json_file)
#     except:
#         pass
#
#     # store percentage values in dict
#     # for method_count, count in method_count_dict.iteritems():
#     #     method_percent_dict[method_count.rstrip().replace("\xe2\x80\x93", "-")] = float(count) / float(
#     #         journal_counts[method_count.rstrip().replace("\xe2\x80\x93", "-")])
#     # print method_count_dict
#     print 'JOURNAL COMPLETED ' + str(journalDirectory)
#     print (str(journalDirectory), method_count_dict)
# # print np.load('method_count_dict.npy')

#print process(pdf_path, language='eng')
# testDir = 'F:/Dropbox/Dropbox/all papers/chi_1col/CHI-2010/p619-takeuchi.pdf'
# try:
#     pdf_text = process(testDir, encoding='utf-8')
# except:
#     pdf_text = ''
# print pdf_text
# for file in os.listdir(testDir):
#     print file
#     process(testDir+"/"+file)
json_file = open('method_count_dict.txt', 'r')
mydict = json_file.readline()
print mydict
print("--- %s seconds ---" % (time.time() - start_time))

# method_occurences = {}
# # for method, count in method_count_dict.iteritems():
# #     for method2 in stat_methods:
# #         if method == method2:
# #             method_occurences.append(count)
# for method in stat_methods:
#     method_occurences[method] = method_count_dict[method]
# stat_column = Column(name='Management of Science', data=list(method_occurences.values()))
# stat_table.add_column(stat_column)
#
# print ascii.write(stat_table, format='fixed_width')


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
