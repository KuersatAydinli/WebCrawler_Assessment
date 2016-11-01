import scraperwiki
import urllib
import urllib2
import re
from BeautifulSoup import BeautifulSoup

journals = ['http://jom.sagepub.com/content/current', 'http://www.journals.uchicago.edu/toc/ajs/current']

scrape = scraperwiki.scrape('http://jom.sagepub.com/content/current')

sample_pdf = urllib.urlretrieve('http://jom.sagepub.com/content/40/1/5.full.pdf+html')
print sample_pdf

#Pring links using urllib2
print '====== Print Link using URLLIB2 ======'
website = urllib2.urlopen('http://jom.sagepub.com/content/40/1.toc')
html = website.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)
print links

print '====== Print Link using BeautifulSoup ======'
#Print links using BeautifulSoup
html_site = urllib2.urlopen('http://jom.sagepub.com/content/40/1.toc')
soup = BeautifulSoup(html_site)
link_list = []
for link in soup.findAll('a'):
    link_list.append(link.get('href'))
print link_list

#Using urllib2 to download PDF link
print '====== Download PDF using urllib2 ======'
def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

download_file('http://jom.sagepub.com/content/40/1/5.full.pdf')




