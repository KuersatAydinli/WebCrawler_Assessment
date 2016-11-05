# -*- coding: utf-8 -*-
import os
from textract import process
from astropy.table import Table, Column
import numpy as np
from astropy.io import ascii

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
        method_synon_dict = self.create_stat_method_dict() # Key: stat. method - Value: acronyms, synonyms

        method_bool_mapping = {}
        for method in methods:
            method_bool_mapping[method] = False # Initialize all values to False for all stat. methods

        pdf_text = process(pdf_path, language='eng')

        for key, values in method_synon_dict.iteritems():
            if len(values) >=1:
                for value in values:
                    if value in pdf_text:
                        method_bool_mapping[key] = True


    def create_initial_table(self):
        """
        Create initial empty Table for final analysis
        """
        method_names = self.get_method_names()
        table = Table()
        method_column = Column(name='stat. Methods', data=method_names)
        table.add_column(method_column)
        journal_names = os.listdir(self.rootdir)
        journal_columns = []
        strs = ["" for x in range(31)] # empty string as default entry for table cell
        for journal in journal_names:
            journal_column = Column(name=journal, data=strs)
            journal_columns.append(journal_column)
        table.add_columns(journal_columns)
        #print ascii.write(table, format='fixed_width')

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
