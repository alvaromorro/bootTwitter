#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TwitterApi import *

api = TwitterApi()

#Buscamos tweets por palabras clave y obtenemos el JSON con los datos de los tweets
results = api.search(5)

#Hacemos RT a los tweets
for tweet in results:
    try:
        api.retweet(tweet)
        api.fav(tweet)
        api.follow(tweet)
    except Exception, e:
        print e
