import os
from textract import process
from astropy.table import Table, Column
import numpy as np

t = Table(names=('a', 'b', 'c'), dtype=('f4', 'i4', 'S2'))
print t


# with open('methodlist_full.csv', 'r') as method_file:
#     for line in method_file.readlines():
#         print line.split(',')[0]

# function: Initialize table, fill table with journal names
# function: fill first column row with method names
class StatPDFPreProcessing:
    rootdir = 'F:/Dropbox/Dropbox/all papers'

    def getBoolean_per_Method(self, pdf_path, *methods):
        # Get text of PDF
        text = process(pdf_path, language='eng')


# #rootdir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs'
rootdir = 'F:/Dropbox/Dropbox/all papers'
#
# Add the three Journals also to all papers directory
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
