#!/usr/bin/env python3
import requests
print('\n\t'+(requests.Session().get('http://ipecho.net/plain', headers='')).text+'\n')
