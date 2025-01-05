# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:47:01 2025

@author: Lewis Colwill

Scrape local election results to help identify wards that may be winnable by the far-right
"""

# Import packages
import requests
from bs4 import BeautifulSoup
import scrapy as sp
import pandas as pd
import re

# Set urls for...

# Open Council Data
open_council_url = "https://opencouncildata.co.uk/byelections.php"

# Local Elections Archive Project
leap_url = "https://www.andrewteale.me.uk/leap/elections-index/"


# Extract text
encoding = b'utf8'
encoding_str = encoding.decode('ascii')

open_council_html = requests.get(open_council_url).content.decode("utf-8")
open_council_sel = sp.Selector(text=open_council_html)
open_council_soup = BeautifulSoup(open_council_html)
open_council_table = open_council_soup.find('table')
open_council_headings = [result.get_text() for result in open_council_table.find_all("th")]
open_council_data = [result.get_text() for result in open_council_table.find_all("td")]#[:5]
open_council_data = [open_council_data[i*len(open_council_headings):(i+1)*len(open_council_headings)] for i in range(int(len(open_council_data)/len(open_council_headings)))]
open_council_df = pd.DataFrame(open_council_data, columns=open_council_headings)

leap_html = requests.get(leap_url).content
leap_soup = BeautifulSoup(leap_html)
leap_list = leap_soup.find_all('li')[::2]
leap_keys = [re.findall("^+(?!\:)", result.get_text()) for result in leap_list]
