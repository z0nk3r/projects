#!/usr/bin/env python3

import re
import time
import requests
import argparse
from bs4 import BeautifulSoup as bs
#from BeautifulSoup import BeautifulSoup as bs
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__author__ = 'z0nk3r'

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    }
)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  cleanertext = re.sub(r'\n\s*\n', '\n\n', cleantext)
  cleanesttext = re.sub(r'&nbsp;', '', cleanertext)
  return cleanesttext.replace("\n\n", "\n")

def args():
	parser = argparse.ArgumentParser(
		description='BAH Calc Scraper',
		epilog=' Example: ./bah.py -y 21 -z 30905 -r E6')
	parser.add_argument('-y', '--year', help= "Enter a Year to Query. If Year is not specified, current year will be used instead.")
	parser.add_argument('-z', '--zip', required=True, help= "Enter a ZIP Code. Try to pick ZIP Code of Duty Station")
	parser.add_argument('-r', '--rank', required=True, help= "Enter a Rank to Compare Against (E1=1, E6=6, E9=9, WO1=10, CW5=14, O1E=15, O3E=17, O1=18, O6=23, O7+=24)")
	args = parser.parse_args()
	return args

def rankconvert(rank):
	rank=rank.upper().replace("-", "").replace('0', 'O')
	rank_dict={'E1': 1,'E2': 2,'E3': 3,'E4': 4, 'E5': 5, 'E6': 6, 'E7': 7, 'E8': 8, 'E9': 9, 'WO1': 10, 'CW2': 11, 'CW3': 12, 'CW4': 13, 'CW5': 14, 'O1E': 15, 'O2E': 16, 'O3E': 17, 'O1': 18, 'O2': 19, 'O3': 20, 'O4': 21, 'O5': 22, 'O6': 23, 'O7': 24, 'O8': 24, 'O9': 24}
	if rank in rank_dict.keys():
		return rank_dict[rank]
	else:
		raise ValueError('Rank ('+str(rank)+') not recognized. Please fix any errors or typos.')

args=args()

if args.year:
	year=args.year
else:
	year=time.strftime("%y", time.localtime())
	
data='YEAR='+str(year)+'&Zipcode='+str(args.zip)+'&Rank='+str(rankconvert(args.rank))+'&submit2=CALCULATE'
print(cleanhtml(requests.get('https://www.defensetravel.dod.mil/pdcgi/bah/bahsrch.cgi', headers=headers, params=data, verify=False).text))