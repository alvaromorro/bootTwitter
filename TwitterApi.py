#Clase para acceder a la API de twitter
# -*- coding: utf-8 -*-
import requests
import json
import tweepy
import pymongo
from credenciales import *
from pymongo import MongoClient


class TwitterApi:

    requests.packages.urllib3.disable_warnings()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    #La url base de la API de twitter
    base_url = 'https://api.twitter.com/'

    auth_url = '{}oauth2/token'.format(base_url)
    search_url = '{}1.1/search/tweets.json'.format(base_url)

    query_es = 'sorteo%20key%20steam%20RT'
    query_en = 'giveaway%20key%20steam%20RT'

    #Inicializar la base de datos
    client = MongoClient()
    client = MongoClient('localhost', 27017)

    db = client.database
    siguiendo= db.siguiendo
    retwiteado = db.retwiteado
    favoritos = db.favoritos

    siguiendo.insert_one({"user_id": 0000})
    retwiteado.insert_one({"tweet_id": 0000})
    favoritos.insert_one({"tweet_id": 0000})

    #Funciones para acceder a la API de Twitter y realizar operaciones
    def search(self,numero_tweets):
        resp = self.api.search(q=self.query_en, count = numero_tweets)
        return resp

    def retweet(self, tweet):
        tweet_id = str(tweet.id)
        if self.retwiteado.find_one({"tweet_id": tweet_id}) == None:
            #NO está en la lista
            try:
                #Hacemos RT y añadimos el id del Tweet a la base de datos
                self.api.retweet(tweet.id)
                self.retwiteado.insert_one({"tweet_id": tweet_id})
                print 'rt'
            except Exception, e:
                print e
                self.retwiteado.insert_one({"tweet_id": tweet_id})
        else: print -1

    def follow(self,tweet):
        user_id = str(tweet.user.id)
        if self.siguiendo.find_one({"user_id": user_id}) == None:
            try:
                self.api.create_friendship(tweet.user.id)
                self.siguiendo.insert_one({"user_id": user_id})
                print 'follow'
            except Exception, e:
                print e
                self.siguiendo.insert_one({"user_id": user_id})
        else: print -1


    def fav(self,tweet):
        tweet_id = str(tweet.id)
        if self.favoritos.find_one({"tweet_id": tweet_id}) == None:
            #NO está en la lista
            try:
                self.api.create_favorite(tweet.id)
                self.favoritos.insert_one({"tweet_id": tweet_id})
                print 'fav'
            except Exception, e:
                print e
                self.favoritos.insert_one({"tweet_id": tweet_id})
        else: print -1

    def test(self,tweet):
        print tweet.user_mentions
