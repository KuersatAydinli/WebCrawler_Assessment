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


# with open('methodlist_full.csv', 'r') as method_file:
#     for line in method_file.readlines():
#         print line.split(',')[0]

# function: Initialize table, fill table with journal names
# function: fill first column row with method names
class StatPDFPreProcessing:

    rootdir = 'F:/Dropbox/Dropbox/all papers'
    stat_method = 'methodlist_full.csv'
    stat_method_dict = {}

    def getBoolean_per_Method(self, pdf_path, *methods):
        # Get text of PDF
        text = process(pdf_path, language='eng')

    def create_initial_table(self):
        method_names = []
        with open(self.stat_method,'r') as method_file:
            for line in method_file.readlines():
                method_names.append(line.split(',')[0])
        # table = Table(data=method_names,names=('stat. Methods'))
        table = Table()
        method_column = Column(name='stat. Methods', data=method_names)
        table.add_column(method_column)
        journal_names = os.listdir(self.rootdir)
        journal_columns = []
        strs = ["" for x in range(31)]
        for journal in journal_names:
            journal_column = Column(name=journal, data=strs)
            journal_columns.append(journal_column)
        table.add_columns(journal_columns)
        # t = Table(names=('statistical Method',os.listdir(self.rootdir)))
        # with open('final_analysis.txt', 'w') as final_analysis:
        #     final_analysis.write(ascii.write(table))
        print ascii.write(table)

    def create_stat_method_dict(self):
        with open(self.stat_method, 'r') as file:
            for line in file.readlines():
                self.stat_method_dict[line.split(',')[0]] = line.split(',')[1:]


statPreProcessor = StatPDFPreProcessing()
stat_table = statPreProcessor.create_initial_table()
# stat_method_dict = statPreProcessor.create_stat_method_dict()


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
