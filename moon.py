#!/usr/bin/env python3
import os
import sys
import time
import requests

__author__='z0nk3r'

while True:
        os.system('clear')
        os.system('date')
        os.system('curl -s http://wttr.in/Moon | head -24')
        time.sleep(90)
