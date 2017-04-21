from lxml import html
import requests
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import re
import time

list_of_titles = []

html = urllib2.urlopen('http://www.richardreddingantiques.com/artworks/')
soup = '%s'%BS(html)
contents = re.findall(r'<span class="content">(.*)</span>', soup)
links = re.findall(r'<a href="(.*/categories/.*)">', soup)

true_links = ['http://www.richardreddingantiques.com%s'%x for x in links]

content_title_dict = {}

for link in true_links[:1]:
    html = urllib2.urlopen(link)
    soup = '%s'%BS(html)
    titles = re.findall(r'<span class="title"><span class="title">(.*)<span class="title_comma"><span class="comma">?', soup)
    content_title_dict[]
    time.sleep(2)

    print 'Waiting for 2 seconds...'

# print links, '\n', true_links
# print soup

