#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import requests
import json

from credenciales import *

key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

requests.packages.urllib3.disable_warnings()

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

# Realizamos la petición y comprobamos el código de respuesta
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

if auth_resp.status_code == 200:
    print 'Conexión establecida'

access_token = auth_resp.json()['access_token']

#Buscamos tweets por palabras clave
search_url = '{}1.1/search/tweets.json'.format(base_url)

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params_es = {
    'q': 'sorteo%20clave%20steam%20RT',
    'result_type': 'recent',
    'count': 10
}

search_params_en = {
    'q': 'giveaway%20key%20steam%20RT',
    'result_type': 'recent',
    'count': 10
}

search_resp = requests.get(search_url, headers=search_headers, params=search_params_en)
print search_resp.status_code

tweet_data = search_resp.json()



for t in tweet_data['statuses']:
    tweet_id = str(t['id'])
    rt_url = '{}1.1/statuses/retweet/:'+tweet_id+'.json'
    rt_url = rt_url.format(base_url)
    print(rt_url)
    #hacer follow, RT, y FAV
