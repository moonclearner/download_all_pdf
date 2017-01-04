# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib2
import re
import os

# open the url and read
def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    page.close()
    return html

# compile the regular expressions and find
# all stuff we need
def getUrl(html):
    reg = r'(?:href|HREF)="?((?:http://)?[^<]+?\.pdf)'
    url_re = re.compile(reg)
    url_lst = re.findall(url_re,html)
    return(url_lst)

def getFile(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')

    # block_sz = 8192
    while True:
        buffer = u.read()
        # buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print "Sucessful to download" + " " + file_name




root_url = "http://cs229.stanford.edu/"

raw_url = "http://cs229.stanford.edu/materials.html"

html = getHtml(raw_url)
url_lst = getUrl(html)

localpath=os.getcwd()
filename="all_pdf_download"
wholepath=os.path.join(localpath,filename)
if not os.path.exists(wholepath):
	os.mkdir('all_pdf_download')
os.chdir(wholepath)

for url in url_lst:
	if url.startswith("http"):
		print url
	else:
		url=root_url+url
		print url
		getFile(url)



