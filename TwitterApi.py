#Clase para acceder a la API de twitter

import base64
import requests
import json

from credenciales import *

class TwitterApi:
    #Usamos las credenciales para crear las keys para poder autenticarnos
    key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {
        'grant_type': 'client_credentials'
    }


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

    #La url base de la API de twitter
    base_url = 'https://api.twitter.com/'

    auth_url = '{}oauth2/token'.format(base_url)
    search_url = '{}1.1/search/tweets.json'.format(base_url)

    def autenticacion(self):
        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
        return auth_resp.status_code

    def search(self):
        search_resp = requests.get(search_url, headers=search_headers, params=search_params_en)
        return search_resp.json()
