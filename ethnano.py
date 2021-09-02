#!/usr/bin/env python3

import os
import sys
import time
import json
import requests

__author__='z0nk3r'

# This script is only applicable to ETH Miners using NANOPOOL as their mining pool.
# Replace the two values below to make it work

account_id='<eth_hash_account_id>'
current_portfolio_value=<your_current_portfolio_value>

while True:
	try:
		j=json.loads((requests.Session().get('https://api.nanopool.org/v1/eth/user/'+str(account_id), headers='')).text)
		ethcalc=json.loads((requests.Session().get('https://api.nanopool.org/v1/eth/approximated_earnings/'+str(j['data']['avgHashrate']['h6']), headers='')).text)
		
		os.system('clear')
		ethtousd=ethcalc['data']['prices']['price_usd']
		os.system('date')
		print('\n\n\t\t=================== NANOPOOL STATS ===================')
		print('\n\n\tETH to USD:\t\t$' + str(ethtousd))
		print('\tCurrent ETH Balance:\t' + str(j['data']['balance']))
		print('\tCurrent USD Balance:\t$' + str(round(float(j['data']['balance'])*float(ethtousd), 2)))
		print('\n\tETH Balance Remaining:\t' + str(round(0.2-float(j['data']['balance']), 8)))
		print('\tCashout Amount:\t\t$' + str(round(ethtousd*0.2, 2)))
		cashouthours=(0.2-float(j['data']['balance']))/float(ethcalc['data']['hour']['coins'])
		if cashouthours > 24:
			print('\tCashout DYs Remaining:\t'+str(round(cashouthours/24, 5)))
		else:
			print('\tCashout HRs Remaining:\t'+str(round(cashouthours, 4)))
		minedtotal=float(current_portfolio_value)
		try:
			if float(lastvalue) > float(j['data']['balance']):
				minedtotal += lastvalue
				print("\n\tETH Mined so Far:\t"+str(round(float(minedtotal), 5)))
				print("\tUSD Earned so Far:\t$"+str(round(float(minedtotal)*float(ethtousd), 2)))
			else:
				print("\n\tETH Mined so Far:\t"+str(round(float(minedtotal) + float(j['data']['balance']), 8)))
				print("\tUSD Earned so Far:\t$"+str(round((float(minedtotal) + float(j['data']['balance']))*float(ethtousd), 2)))			
		except:
			print("\n\tInitializing...\n")
		
		print('\n\tAvg Hashrates:')
		print('\n\t\t24H\t12H\t6H\t3H\t1H')
		print('\t\t'+str(j['data']['avgHashrate']['h24'])+'\t'+str(j['data']['avgHashrate']['h12'])+'\t'+str(j['data']['avgHashrate']['h6'])+'\t'+str(j['data']['avgHashrate']['h3'])+'\t'+str(j['data']['avgHashrate']['h1']))
		print('\n\t===================== Hashrate Earnings Averages (6H) ======================\n')
		print('\t\tYEAR\t\tMONTH\t\tWEEK\t\tDAY\t\tHOUR')
		print(f"\tUSD:\t${str(round(ethcalc['data']['month']['dollars']*12, 2)):15s}${str(round(ethcalc['data']['month']['dollars'], 2)):15s}${str(round(ethcalc['data']['week']['dollars'], 2)):15s}${str(round(ethcalc['data']['day']['dollars'], 2)):15s}${str(round(ethcalc['data']['hour']['dollars'], 2)):15s}") 
		print(f"\tETH:\t{str(round(ethcalc['data']['month']['coins']*12, 4)):16s}{str(round(ethcalc['data']['month']['coins'], 4)):16s}{str(round(ethcalc['data']['week']['coins'], 4)):16s}{str(round(ethcalc['data']['day']['coins'], 4)):16s}{str(round(ethcalc['data']['hour']['coins'], 7)):16s}") 
		try:
			lastvalue=j['data']['balance']
		except:
			print("\n\tLastvalue set failed")
						
	except:
		os.system('date')
		print('\n\n\t\t=================== NANOPOOL STATS ===================')
		print('\n\n\t[!] Unable to connect to Nanopool API. \n\t[X] Slow the poll rate, check the worker, or check your net connection.')
	
	time.sleep(15)


