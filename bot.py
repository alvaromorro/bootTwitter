#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import json
from TwitterApi import *

api = TwitterApi()

auth_code = api.autenticacion()

if auth_code == 200:
    print 'Conexión establecida'
else: print 'Error'+ str(auth_code)
#access_token = auth_resp.json()['access_token']

#Buscamos tweets por palabras clave
search_resp = api.search

print search_resp

tweet_data = search_resp.json()

for t in tweet_data['statuses']:
    tweet_id = str(t['id'])
    rt_url = '{}1.1/statuses/retweet/:'+tweet_id+'.json'
    rt_url = rt_url.format(base_url)
    print(rt_url)
    #hacer follow, RT, y FAV
