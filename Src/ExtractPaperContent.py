from __future__ import division

import ast
import os
import string
import time

from astropy.io import ascii
from astropy.table import Table, Column
from textract import process


class ExtractPaperContent():
    rootdir = 'F:/Dropbox/Dropbox/all papers'
    rootdir_txt = 'F:/all_papers_txt'

    def extract_all_content(self):
        counter = 1
        for journal in os.listdir(self.rootdir):
            for sub_dir in os.listdir(self.rootdir+'/'+journal):
                for paper in os.listdir(self.rootdir+'/'+journal+'/'+sub_dir):
                    try:
                        pdf_text = process(self.rootdir+'/'+journal+'/'+sub_dir+'/'+paper, language='eng')
                    except:
                        pdf_text = ''
                    if not os.path.exists(self.rootdir_txt+'/'+journal+'/'+sub_dir):
                        os.makedirs(self.rootdir_txt+'/'+journal+'/'+sub_dir)
                    with open(self.rootdir_txt+'/'+journal+'/'+sub_dir+'/'+paper[:-4]+'.txt','w') as pdf_content:
                        pdf_content.write(pdf_text)
                    print ('EXTRACTED: ' + self.rootdir+'/'+journal+'/'+sub_dir+'/'+paper, counter)
                    counter += 1

extractor = ExtractPaperContent()
extractor.extract_all_content()