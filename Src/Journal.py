# -*- coding: utf-8 -*-
import os


class Journal():
    rootdir = 'F:/Dropbox/Dropbox/all papers'
    stat_method = 'methodlist_full.csv'

    @staticmethod
    def initialize_journal_method_dict(self):
        journal_method_dict = {}
        method_paper_dict = {}
        with open(self.stat_method, 'r') as file:
            for line in file.readlines():
                method_paper_dict[line.split(',')[0]] = []

        for journal in os.listdir(self.rootdir):
            journal_method_dict[journal] = method_paper_dict
        return journal_method_dict

    def get_paper_counts_per_journal(self):
        journal_counts = {}
        for journal in os.listdir(self.rootdir):
            journal_counts[journal] = sum([len(files) for r, d, files in os.walk(self.rootdir + "/" + journal)])

journalClass = Journal()
journal_method_dict = journalClass.initialize_journal_method_dict(journalClass)
print journal_method_dict
print len(journal_method_dict.keys())