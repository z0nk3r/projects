#!/usr/bin/env python3
import os
import sys
import argparse

__author__='z0nk3r'
	
def args():
	parser = argparse.ArgumentParser(epilog=' Example: 64d randomtext==')
	parser.add_argument('string', help= "Enter a string to be decoded!")
	parser.add_argument('-d','--decode', action='store_true', help= "Use this to decode messages!")
	return parser.parse_args()
if args().decode is True:
	os.system('echo '+str(args().string)+' | base64 -d;echo ""')
else:
	os.system('echo '+str(args().string)+' | base64;echo ""')
