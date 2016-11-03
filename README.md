# WebCrawler_Assessment
This repository is primarily responsible for the development of a Python webcrawler which is used to download PDF files from dedicated journal websites,
namely the 'Journal of Mangement', the 'American Journal of Sociology' and the 'Management of Science'.

# Idea behind Implementation
For a given journal website, the very first thing to do is to smartly extract links which lead to the desired PDF files.
Once ensured that a list of relevant links is stored, iterate through the list and open the corresponding link and download the PDF file.
The PDF files are stored in DropBox. Cookie Handling enabled from within code

# Implementation
The webcrawler was implemented in Python using the built in 'urllib2' library to download the content of a website

