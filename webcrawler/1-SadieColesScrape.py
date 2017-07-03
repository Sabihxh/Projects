#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as soup
from flpy.utils import include_url, extract_links, make_parent_dirs
import hashlib
import os
import re
import json
import cjson

class perfect_scraper(object):

    _main_website = u'http://www.sadiecoles.com'
    _json_out_file_path = './data/originals/jsons/'
    
    _books = []
    _artists = []
    _exhibition = []
    _news = []

    mapping_artist = {}

    _artist_id_count = 1
    _news_id_count = 1
    _press_id_count = 1
    _exhibition_id_count = 1


    def __init__(self):
        pass



    def run_fucntions(self):
        self._scrape_artists()
        self._scrape_exhibitions()
        # self.date_fix()

    def open_and_soup(self, link):
        "Returns the soup of the link"

        open_url = requests.get(link, verify = False)
        read_url = open_url.text
        return soup(read_url, 'html.parser')


    def _scrape_artists(self, artist_link = "http://www.sadiecoles.com/artists.html"):
        artist_html = self.open_and_soup(artist_link)
        all_artists_list = artist_html.find('ul', {"class": "artist-list"})

        for artist_data in all_artists_list.find_all("li"):

            temp_dict = {}

            artist_links = artist_data.find("span", {"class": "english-content"})
            artist_name = artist_links.text.strip()
            temp_dict['name'] = artist_name
            fetch_image = artist_data.find("div", {"class": "artist-preview"})

            if fetch_image:
                artist_image_override = self._main_website + fetch_image.img.get("src")

                "IMAGES ARE BEING DOWNLOADED to wrong folder path (maybe correct) but it needs to be checked - Thursday"
                image_hash = hashlib.md5(artist_image_override).hexdigest()
                image_path = '/ClientDocuments/sites/sadiecoles/usr/public/images/artworks/main_image/items/%s/%s'%(image_hash, artist_image_override)
                self.download_image(artist_image_override, image_path)

            #Make url for artist to be used to match exhibitions
            get_artist_link = artist_data.a
            if get_artist_link:
                
                artist_link = self._main_website + get_artist_link.get("href")
                artist_page_html = self.open_and_soup(artist_link)
                artist_exhibs = artist_page_html.find("ul", {"class": "exhibitions"})

                for stuff in artist_exhibs.find_all("li"):
                    stuff_url = stuff.a.get("href")
                    url_end = stuff_url.rsplit(u'/', 1)
                    if url_end:
                        artist_exhi_relation_url = self._main_website + u'/artists' u'/%s'%artist_name.split()[-1] + '#' + url_end[-1]

                    # if artist_name not in self.mapping_artist:
                    #     self.mapping_artist[artist_name] = []
                    self.mapping_artist[artist_exhi_relation_url.lower()] = self._artist_id_count
            
            temp_dict['id'] = self._artist_id_count
            self._artists.append(temp_dict)
            self._artist_id_count += 1
        print self._artists
        # print self.mapping_artist


    def _scrape_exhibitions(self):

        splitters = [u'—', u'–', u'-']

        for year in range(1997, 2018):
            url = self._main_website + u'/exhibitions/%s'%year + u'.html'
            whole_page_html = self.open_and_soup(url)
            exhibs_html = whole_page_html.find("div", {"class", "eight exhibition-list columns"})

            for exhib in exhibs_html.div.find_all("section"):
                temp_dict = {}
                artist_url_ID = exhib.find_all("div", {"class": "eight columns"})
                
                for data in artist_url_ID:
                    artist_url = data.img.get('data-image-link')
                    if artist_url.lower() in self.mapping_artist:
                        if 'selected_artists' not in temp_dict:
                            temp_dict['selected_artists'] = []
                        temp_dict['selected_artists'].append(self.mapping_artist[artist_url])

                exhib_name_holder = exhib.find("span", {"class": "english-content name"})
                if exhib_name_holder:
                    exhib_name = exhib_name_holder.text


                chinese_exhib_name_holder = exhib.find("span", {"class": "chinese-content name chinese-name"})
                if chinese_exhib_name_holder:
                    chinese_exhib_name = chinese_exhib_name_holder.text

                exhib_subtitle_name_holder = exhib.find("span", {"class": "subtitle english-content"})
                if exhib_subtitle_name_holder:
                    exhib_subtitle = exhib_subtitle_name_holder.text
                    

                chinese_subtitle_name_holder = exhib.find("span", {"class": "subtitle chinese-content"})
                if chinese_subtitle_name_holder:
                    chinese_subtitle = chinese_subtitle_name_holder.text

                exhib_date_holder = exhib.find("span", {"class": "date english-content"})

                # -------- Get Exhib Date --------#
                if exhib_date_holder.text:
                    # exhib_start_date = date_fix(exhib_date_holder.text)[0]
                    # exhib_end_date = date_fix(exhib_date_holder.text)[1]
                    for splitter in splitters:
                        if splitter in exhib_date_holder.text:
                            exhib_start_date_unformatted = exhib_date_holder.text.split(splitter)[0]
                            exhib_end_date_unformatted = exhib_date_holder.text.split(splitter)[-1]

                            temp_st_date = exhib_start_date_unformatted.split()
                            temp_en_date = exhib_end_date_unformatted.split()

                            if len(temp_st_date) >= 2 and temp_st_date[0].isdigit() and temp_st_date[1].isalpha():
                                exhib_start_date = u'%s-'%year + u'%s'%self.month_num(temp_st_date[1]) + u'-%s'%temp_st_date[0]

                            elif len(temp_st_date) == 1 and temp_st_date[0].isdigit() and len(temp_en_date) > 1:
                                exhib_start_date = u'%s-'%year + u'%s'%self.month_num(temp_en_date[1]) + u'-%s'%temp_st_date[0]

                            elif len(temp_st_date) == 1 and temp_st_date[0].isalpha() and len(temp_en_date) > 1:
                                exhib_start_date = u'%s-'%year + u'%s'%self.month_num(temp_st_date[0]) + u'-01'
                            
                            if len(temp_en_date) == 3:
                                exhib_end_date = u'%s-'%temp_en_date[2] + u'%s-'% self.month_num(temp_en_date[1]) + u'%s'%temp_en_date[0]

                    s_date_check = exhib_start_date.split('-')
                    for item in s_date_check:
                        if not item.isdigit():
                            exhib_start_date = ''

                    e_date_check = exhib_end_date.split('-')
                    for item in e_date_check:
                        if not item.isdigit():
                            exhib_end_date = ''

                e_location_holder = exhib.find("span", {"class": "location english-content"})                
                if e_location_holder:
                    e_location = e_location_holder.getText(separator=', ')

                temp_dict['location'] = e_location or u''
                temp_dict['start_date'] = exhib_start_date or u''
                temp_dict['end_date'] = exhib_end_date or u''
                temp_dict['title'] = exhib_name.strip() or u''
                temp_dict['subtitle'] = exhib_subtitle.strip() or u''

                self._exhibition.append(temp_dict)
        print self._exhibition
        
                


    def download_image(self, website_img_url, artlogic_img_filepath): 

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

    def month_num(self, month):

        month_mappings = {  
                            u'January': u'01',
                            u'February': u'02',
                            u'March': u'03',
                            u'April': u'04',
                            u'May': u'05',
                            u'June': u'06',
                            u'July': u'07',
                            u'August': u'08',
                            u'September': u'09',
                            u'October': u'10',
                            u'November': u'11',
                            u'December': u'12'
                        }
        return month_mappings.get(month)

    def _check_link_for_validity(self, link):
        """This function takes a link and checks if returns True if valid, otherwise False.
        e.g. _check_link_for_validity('http://google.com') should return True"""
        is_valid = True
        response = requests.get(link)
        if response.status_code == 200:
            is_valid = True
        return is_valid


    def _create_json_file(self, list_items, filepath):
        json_data = json.dumps(list_items, indent=4, ensure_ascii=False).encode('utf8')
        file = open(filepath, 'w')
        file.write(json_data)
        file.close()

    def _create_json_files_from_data(self):
        if self._artists:
            self._create_json_file(self._artists, os.path.join(self._json_out_file_path, 'artists.json'))
        if self._artworks:
            self._create_json_file(self._artworks, os.path.join(self._json_out_file_path, 'artworks.json'))
        if self._news:
            self._create_json_file(self._news, os.path.join(self._json_out_file_path, 'news.json'))
        if self._press:
            self._create_json_file(self._press, os.path.join(self._json_out_file_path, 'press.json'))
        if self._exhibitions:
            self._create_json_file(self._exhibitions, os.path.join(self._json_out_file_path, 'exhibitions.json'))



i = perfect_scraper()

i.run_fucntions()








