from __future__ import division

import ast
import os
import re
import string

import time

from astropy.io import ascii
from astropy.table import Table, Column
from textract import process


class StatPDFPreProcessing:
    rootdir = 'F:/Dropbox/Dropbox/all papers'
    stat_method = 'methodlist_full.csv'

    def create_method_bool_dict_on_txt(self, pdf_path, methods):
        method_synon_dict = self.create_stat_method_dict()  # Key: stat. method - Value: list of acronyms, synonyms

        method_bool_mapping = {}
        for method in methods:
            method_bool_mapping[method] = False  # Initialize all values to False for all stat. methods

        pdf_text = re.sub(r'\s+', ' ', open(pdf_path, 'r').read())

        for key, values in method_synon_dict.iteritems():
            # list of all possible permutation per string to be checked if it is existent in paper
            regex_list = []
            for value in values:
                regex_list.append(re.sub(r'\s+', ' ', value).rstrip())
            regex_list.append(re.sub(r'\s+', ' ', key).rstrip())
            for i, regex in enumerate(regex_list):
                if regex != "" and regex.lower() != " CI".lower():
                    if pdf_text.lower().translate(None, string.punctuation).rstrip().find(
                            regex.lower().translate(None, string.punctuation)) != -1:
                        method_bool_mapping[key] = True

        return method_bool_mapping

    def create_method_bool_dict(self, pdf_path, methods):
        """

        :rtype: dict per paper: dictionary with statistical method as key and boolean for occurence in paper as value
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
            # list of all possible permutation per string to be checked if it is existent in paper
            regex_list = []
            for value in values:
                regex_list.append(value.rstrip().replace("\xe2\x80\x93", "-"))
            regex_list.append(key.rstrip().replace("\xe2\x80\x93", "-"))
            for i, regex in enumerate(regex_list):
                if regex != "" and regex.lower() != "CI".lower():
                    if pdf_text.lower().translate(None, string.punctuation).rstrip().replace("\xe2\x80\x93", "-").find(
                            regex.lower().translate(None, string.punctuation)) != -1:
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

statPreProcessor = StatPDFPreProcessing()
stat_table = statPreProcessor.create_initial_table()
method_dict = statPreProcessor.create_stat_method_dict()
stat_methods = statPreProcessor.get_method_names()
method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt('paper1.txt', stat_methods)
print method_bool_dict

# ======================================= START: Process Statistical Analysis on all Papers ===============================================
testDir = 'F:/Dropbox/Dropbox/all papers/Management of Science'
main_dir = 'F:/all_papers_txt_new'

counter = 1

journal_counts = {}
for journal in os.listdir(main_dir):
    journal_counts[journal] = sum([len(files) for r, d, files in os.walk(main_dir + "/" + journal)])
print journal_counts

journal_method_tuple = []

for journalDirectory in os.listdir(main_dir):
    method_count_dict = {}  # count in how many papers a stat. method appears: Key: method - Value: #Papers
    method_percent_dict = {}  # same as method_count_dict - only with percentage values
    for method in stat_methods:
        method_count_dict[method.rstrip().replace("\xe2\x80\x93", "-")] = 0

    for month_issue in os.listdir(main_dir + "/" + journalDirectory):
        for file in os.listdir(main_dir + "/" + journalDirectory + '/' + month_issue):
            method_bool_dict = statPreProcessor.create_method_bool_dict_on_txt(
                main_dir + "/" + journalDirectory + "/" + month_issue + "/" + file,
                stat_methods)
            print (journalDirectory, month_issue, file, counter)
            for method, occ in method_bool_dict.iteritems():
                if occ == True:
                    # print (method, file)
                    method_count_dict[method.rstrip().replace("\xe2\x80\x93", "-")] += 1
            counter += 1

    journal_method_tuple.append((journalDirectory, method_count_dict))
    print 'JOURNAL COMPLETED ' + str(journalDirectory)
    print (str(journalDirectory), method_count_dict)

with open('final_analysis_new_second.txt', 'w') as final_analysis:
    final_analysis.write('\n'.join('(%s, %s)' % x for x in journal_method_tuple))
# ======================================= END: Process Statistical Analysis on all Papers ===============================================


# ======================================= START: Generate percentage distribution for all journals ======================================

# journal_counts = {}
# for journal in os.listdir(main_dir):
#     journal_counts[journal] = sum([len(files) for r, d, files in os.walk(main_dir + "/" + journal)])
# print journal_counts
final_table = Table()
final_columns = []
stat_keys = []
with open('final_analysis_new_second.txt', 'r') as final_analysis:
    for line in final_analysis.readlines():
        for jour in journal_counts.keys():
            if jour in line:
                dict_journ = ast.literal_eval(line[len(jour) + 3:][:-1].translate(None, ')'))
                for key, value in dict_journ.iteritems():
                    dict_journ[key] = value / journal_counts[jour]
                # print (jour, dict_journ)
                stat_keys = dict_journ.keys()
                distri_column = Column(name=jour, data=list(dict_journ.values()))
                final_columns.append(distri_column)
print("--- %s seconds ---" % (time.time() - start_time))
stat_column = Column(name='stat. Methods', data=stat_keys)
final_table.add_column(stat_column)
final_table.add_columns(final_columns)
print ascii.write(final_table, format='fixed_width')
ascii.write(final_table, 'final_distribution_new_second.dat', format='fixed_width')
# ======================================= END: Generate percentage distribution for all journals ======================================
