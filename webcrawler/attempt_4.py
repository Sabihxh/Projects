#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as soup
from flpy.utils import include_url, extract_links, make_parent_dirs
import hashlib
import urllib
import requests
from time import sleep
import re
import codecs
import csv
import os
from flpy.utils import hash32

class ScrapeBabyScrape(object):

    main_dict = {}

    def __init__(self):
        pass

    def run(self):
        self.scrape_categories()

    """
    open_url_and_soup_it takes webpage url as link
    and returns the souped version of
    html of that webpage
    """
    def open_url_and_soup_it(self, link):
        #open the connection
        open_that_url = requests.get(link)

        #read the html
        that_urls_html = open_that_url.text
        
        #close the connection
        open_that_url.close()

        #return the souped version of html
        return soup(that_urls_html, 'html.parser')
    
    def scrape_categories(self):
        a_file = codecs.open('./html_files/artworks_from_categories.txt', 'w', 'utf-8')
        headers = ['id', 'title', 'price', 'artwork_detail', 'edition_detail', 'dimensions', 'Category', 'image_name', 'main_image', 'image_hash', 'image_path']
        a_file.write(u"%s\n" % '|'.join(headers))

        main_website = 'http://www.lawrencealkingallery.com/'
        #get the soup of website
        sub_categories_soup = self.open_url_and_soup_it(main_website)
        sub_categories_list = []

        category = sub_categories_soup.find_all('li' ,{"class" : "toplevel toplevelcats"})[0]
        auto_id = 101
        for subcategory in category.find_all('li', {"class": "sublist"}):
            sub_categories_list.append(subcategory.a.get("href"))

        for a_link in sub_categories_list[:1]:
            artwork_links = []
            html = self.open_url_and_soup_it(a_link)

            for b_link in html.find_all('div', {"class" : "artistindexcaption"}):
                artwork_links.append(b_link.a.get("href"))

            #finally itterate through each artwork and get the data
            for actual_artwork_links in artwork_links[:10]:
                row_list = []
                try: artwork_html = self.open_url_and_soup_it(actual_artwork_links)
                except: continue

                image_details = artwork_html.find(class_="fancybox")
                if image_details: image_url = image_details.get("href")
                if image_url: image_name = image_url.rsplit('/', 1)[1]

                try:
                    #contains artwork detail, edition detail and dimension
                    mixed_data = u'%s'%artwork_html.find(class_="productmisc")
                    details_list = u'%s'%re.findall(r'>(.+)<', mixed_data)[0]
                    if details_list: details_list = details_list.split('<br/>')
                except: details_list = ['']*3

                try: 
                    title = artwork_html.find_all("div", {"class" : "producttitleleft"})
                    if title: title = title[0].h1.text
                    else: title = ''
                except: title = ''

                try:
                    price = artwork_html.find_all("p", {"class" : "productprice"})[0].text.replace(',', '')
                    if price: price = price.strip().replace(',', '|')
                    else: price = ''

                except: price = ''

                try: artwork_detail = details_list[0]
                except: artwork_detail = ''

                try: edition_detail = details_list[1]
                except: edition_detail = ''

                try: dimensions = details_list[2]
                except: dimensions = ''
                
                a_category = a_link.rsplit('/', 1)[-1]
                
                # file_path: /usr/public/images/artworks/main_image/items/<id>/<file-name>
                # main_image: /usr/images/artworks/main_image/items/<id>/<file-name>
                fake_image_path = '/Users/artlogic/Desktop/Galleries/LawrenceAlkin/CMS_images/%s'%image_name
                self.download_image(image_url, fake_image_path)

                open_image = open(fake_image_path).read()
                image_hash = hash32(open_image)
                image_path = '/ClientDocuments/sites/lawrencealkin/usr/public/images/artworks/main_image/items/%s/%s/%s'%(image_hash[:4], image_hash, image_name)
                main_image = '/usr/images/artworks/main_image/items/%s/%s/%s'%(image_hash[:4], image_hash, image_name)
                a_row = '%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s'%(auto_id, title, price, artwork_detail, edition_detail, dimensions, a_category, main_image, image_name, image_path, image_hash)
                print a_row
                a_file.write('%s\n'%a_row)
                print 'Downloading image...'
                self.download_image(image_url, '/ClientDocuments/sites/lawrencealkin/usr/public/images/artworks/main_image/items/%s/%s/%s'%(image_hash[:4], image_hash, image_name))
                print 'Download complete', '.../%s/%s'%(auto_id, image_name)
                auto_id += 1
                print '*'*100

        a_file.close()

    def scrape_artist(self):

        csv_file = open("./html_files/artistnames.csv", 'w')
        csv_file.write('Artist\n')
        artist_url = "http://www.lawrencealkingallery.com/artists/all"

        artist_page = urllib.urlopen(artist_url)
        artist_page_html = artist_page.read()

        # print artist_page_html
        artist_page_soup = soup(artist_page_html, 'html.parser')
        c = 1
        for artist in artist_page_soup.find_all("p", {"class": "artistindexname"}):
            print c, artist.text.strip()
            value = artist.text.strip()
            sutf8 = value.encode('UTF-8')
            # print sutf8
            csv_file.write('%s\n'%sutf8)
            c += 1

    def download_image(self, website_img_url, artlogic_img_filepath):
    #        print artlogic_img_filepath
       if os.path.exists(artlogic_img_filepath):
           return True
       make_parent_dirs(artlogic_img_filepath)
       image_bytes = None
       try:
           image_bytes = include_url(website_img_url.replace(' ', '%20'))
       except:
           print 'No image in img_url: %s'%website_img_url
           pass

       if image_bytes:
           f = open(artlogic_img_filepath, 'wb')
           f.write(image_bytes)
           f.close()
           return True
       return False

i = ScrapeBabyScrape()
i.run()







