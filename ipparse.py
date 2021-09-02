#!/usr/bin/env python3
import os
import sys
import json
import requests
import argparse

__author__='z0nk3r'

def args():
	parser = argparse.ArgumentParser(
		description='Retriever/Scraper for IP Data!',
		epilog=' Example: ipparse XXX.XXX.XXX.XXX')
	#parser.add_argument('-i','--ip', help= "Enter An IP Address!")
	parser.add_argument('ip', help= "Enter an IP Address!")
	args = parser.parse_args()
	return args

args=args()
count=1
for item in args.ip.split(','):
	j=json.loads((requests.Session().get('http://ipinfo.io/'+item+'/json', headers='')).text)
	print("\n============================= IP Addr: "+item+" // Item No: "+str(count)+" ================================")
	print("\n =======LOCATION INFO=======\n")
	try:
		print('  [-] COUNTRY:\t' + str(j['country']))
	except:
		print('  [!] COUNTRY:\tNo Information Found')
	try:
		print('  [-] STATE:\t' + str(j['region']))
	except:
		print('  [!] STATE:\tNo Information Found')
	try:
		print('  [-] CITY:\t' + str(j['city']))
	except:
		print('  [!] CITY:\tNo Information Found')
	try:
		print('  [-] ZIPCODE:\t' + str(j['postal']))
	except:
		print('  [!] ZIPCODE:\tNo Information Found')
	try:
		print('  [-] LAT/LON:\t' + str(j['loc']))
	except:
		print('  [!] LAT/LON:\tNo Information Found')
	print('\n =======ISP INFO=======\n')
	try:
		print('  [-] ISP & AS Num:\t' + str(j['org']))
	except:
		print('  [!] ISP & AS Num:\tNo Information Found')
	try:
		print('  [-] HOSTNAME:\t\t' + str(j['hostname'])+'\n')
	except:
		print('  [!] HOSTNAME:\t\tNo Information Found\n')
	count+=1
