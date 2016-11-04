import os
from textract import process


# Hierzu müssten wir für jedes Journal wissen, welche statistische Methode in wie vielen Papers vorkommt.
# Falls eine Methode mehrmals im gleichen Paper vorkommt, wir sie trotzdem nur einmal gezählt. Beispiel: t-test kommt in Management Science in 23% der Paper vor.
# Um die Prozentzahl zu kriegen musst du zuerst den Text vom PDF extrahieren, und dann mit regex nach den besagten stat.
# Methoden suchen. Da bei PDF’s häufig die Leerzeichen etwas fehlerhaft extrahiert werden brauchst du wahrscheinlich regular expressions.

class StatPDFPreProcessing:
    rootdir = 'F:/Dropbox/Dropbox/all papers'

    def getBoolean_per_Method(self, pdf_path, *methods):
        # Get text of PDF
        text = process(pdf_path, language='eng')


        # #rootdir = 'F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs'
        # rootdir = 'F:/Dropbox/Dropbox/all papers'
        #
        # #Add the three Journals also to all papers directory
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
