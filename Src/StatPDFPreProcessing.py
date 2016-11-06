# -*- coding: utf-8 -*-
from __future__ import division
import os

import PyPDF2
import ast

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


# ======================================= START: Process Statistical Analysis on all Papers ===============================================

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
# ======================================= END: Process Statistical Analysis on all Papers ===============================================


# ======================================= START: Generate percentage distribution for all journals ======================================
main_dir = 'F:/Dropbox/Dropbox/all papers'
journal_counts = {}
for journal in os.listdir(main_dir):
    journal_counts[journal] = sum([len(files) for r, d, files in os.walk(main_dir + "/" + journal)])
print journal_counts
final_table = Table()
final_columns = []
stat_keys = []
with open('final_analysis.txt', 'r') as final_analysis:
    for line in final_analysis.readlines():
        for jour in journal_counts.keys():
            if jour in line:
                dict_journ = ast.literal_eval(line[len(jour)+5:][:-2])
                for key, value in dict_journ.iteritems():
                    dict_journ[key] = value/journal_counts[jour]
                print (jour,dict_journ)
                stat_keys = dict_journ.keys()
                distri_column = Column(name=jour, data=list(dict_journ.values()))
                final_columns.append(distri_column)
print("--- %s seconds ---" % (time.time() - start_time))
stat_column = Column(name='stat. Methods', data=stat_keys)
final_table.add_column(stat_column)
final_table.add_columns(final_columns)
print ascii.write(final_table, format='fixed_width')
ascii.write(final_table, 'final_distribution.dat', format='fixed_width')
# ======================================= END: Generate percentage distribution for all journals ======================================