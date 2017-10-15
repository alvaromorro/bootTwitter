#!/usr/bin/env python
# -*- coding: utf-8 -*-

from TwitterApi import *

api = TwitterApi()

#Buscamos tweets por palabras clave y obtenemos el JSON con los datos de los tweets
results = api.search(5)

for t in results:
    api.test(t)

#Hacemos RT a los tweets
def proceso(self):
    for tweet in results:
        try:
            api.retweet(tweet)
            api.fav(tweet)
            api.follow(tweet)
        except Exception, e:
            print e
