# -*- coding: utf-8 -*-
import os
import Journal


class StatMethodSearch():
    stat_method = 'methodlist_full.csv'
    rootdir = 'F:/all_papers_txt'

    def create_stat_method_dict(self):
        """
        Create dict of statistical method and its synonyms
        """
        with open(self.stat_method, 'r') as method_file:
            stat_method_dict = {}
            for line in method_file.readlines():
                stat_method_dict[line.split(',')[0]] = line.split(',')[1:]
        print stat_method_dict
        for k, v in stat_method_dict.iteritems():
            stat_method_dict[k] = self.clean_string(v)
        return stat_method_dict

    def clean_string(self, strings):
        clean_list = []
        for string in strings:
            new_string = string.rstrip().replace("\xe2\x80\x93", "-").replace("\xe2\x80\x99", "’").replace("\xce\xa7",
                                                                                                           "Χ").replace(
                "\xcf\x87", "χ").replace("\xcf\x872", "χ2")
            clean_list.append(new_string)
        return clean_list

    def initialize_journal_dict(self):
        journal_method_dict = {}
        method_paper_dict = {}
        with open(self.stat_method, 'r') as file:
            for line in file.readlines():
                method_paper_dict[line.split(',')[0]] = []

        for journal in os.listdir(self.rootdir):
            journal_method_dict[journal] = method_paper_dict
        return journal_method_dict

    def search_methods(self):
        # journal = Journal.Journal
        # journal_method_dict = journal.initialize_journal_method_dict(journal)
        journal_method_dict = self.initialize_journal_dict()
        stat_method_dict = self.create_stat_method_dict()
        for journal in os.listdir(self.rootdir):
            if journal == 'American Journal of Sociology':
                for key, values in stat_method_dict.iteritems():
                    regex_list = []
                    for value in values:
                        regex_list.append(value)
                    regex_list.append(key.rstrip())

                    for sub_dir in os.listdir(self.rootdir + '/' + journal):
                        found_papers = []
                        for paper in os.listdir(self.rootdir + '/' + journal + '/' + sub_dir):
                            with open(self.rootdir + '/' + journal + '/' + sub_dir + '/' + paper) as paper_txt:
                                for line in paper_txt.readlines():
                                    for regex in regex_list:
                                        if ('CI' not in regex) and (regex != '') and regex in line:
                                            found_papers.append(self.rootdir + '/' + journal + '/' + sub_dir + '/' + paper)
                                            journal_method_dict[journal][regex_list[-1]] = found_papers
        return journal_method_dict


statMethod = StatMethodSearch()
print statMethod.create_stat_method_dict()
print '\xcf\x872'.replace("\xcf\x872", "χ2")
journal_method_dict = statMethod.search_methods()
print journal_method_dict
for k,v in journal_method_dict['American Journal of Sociology'].iteritems():
    print (k,len(v))
