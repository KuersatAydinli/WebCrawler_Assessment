# Works without space characters
# import pyPdf
#
# print 'This is a test'
#
# print 'http://jom.sagepub.com/content/40/2.toc.pdf'[22:] + '+html'
#
# testPDF = "FlashTeams.pdf"
#
# # with open('FlashTeams.pdf') as f:
# #     doc = slate.PDF(f)
# #
# # print doc
#
# pdf = pyPdf.PdfFileReader(open(testPDF, "rb"))
# for page in pdf.pages:
#     print page.extractText()

# BUllSHIT
# import PyPDF2
#
# pdf_file = open('FlashTeams.pdf', 'rb')
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
# number_of_pages = read_pdf.getNumPages()
# page = read_pdf.getPage(0)
# page_content = page.extractText()
# print page_content


# WORKS THE BEST
from textract import process
text = process('F:/Dropbox/Dropbox/WebCrawler_Assessment_PDFs/Management of Science/June/Doc14.pdf')
print text
