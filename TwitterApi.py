#Clase para acceder a la API de twitter
# -*- coding: utf-8 -*-
import requests
import json
import tweepy
import pymongo
from credenciales import *
from pymongo import MongoClient


class TwitterApi:

    retweeted = []
    favorited = []
    following = []

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
    collection = db.test_collection
    collection.insert_one({"texto":"hola"})

    #Funciones para acceder a la API de Twitter y realizar operaciones
    def search(self,numero_tweets):
        resp = self.api.search(q=self.query_es, count = numero_tweets)
        return resp

    def retweet(self, tweet):
        if tweet.id in self.retweeted == False:
            #NO está en la lista
            try:
                self.api.retweet(tweet.id)
                print 'rt'
            except Exception, e:
                print e
                self.retweeted.append(tweet.id)

    def follow(self,tweet):
        if tweet.user.id in self.following == False:
            try:
                self.api.create_friendship(tweet.user.id)
                print 'follow'
            except Exception, e:
                print e
                self.following.append(tweet.user.id)
        else: print 'no in list '

    def fav(self,tweet):
        if tweet.id in self.favorited:
            #NO está en la lista
            try:
                self.api.retweet(tweet.id)
                print 'fav'
            except Exception, e:
                print e
                self.favorited.append(tweet.id)
