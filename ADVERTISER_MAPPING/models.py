# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime

import mysql.connector
import requests
import json
import sys

# Create your models here.
class ADVERTISER_MAPPING(models.Model):
    #PUBLISHER_API_KEY = models.CharField(max_length=200)
    #PUBLISHER_API_URL = models.CharField(max_length=200)
    #affiliate_id = models.CharField(max_length=200)
    #offer_id = models.CharField(max_length=200)
    Advertiser_HASH_ID = models.CharField(max_length=200)
    Title = models.CharField(max_length=1000)
    Tracking_Link = models.CharField(max_length=1000)
    Preview_Link = models.CharField(max_length=1000)
    Description = models.CharField(max_length=1000)
    Countries = models.CharField(max_length=1000)
    Logo = models.CharField(max_length=1000)
    Privacy = models.CharField(max_length=1000)
    Status = models.CharField(max_length=1000)
    Revenue = models.CharField(max_length=1000)
    Payout = models.CharField(max_length=1000)
    Creative_Urls = models.CharField(max_length=1000)
    Caps = models.CharField(max_length=1000)
    Freshness = models.CharField(max_length=1000)
    Strict_Or_Not = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "CREATE OR UPDATE ADVERTISER"

# class CREATE_API(models.Model):
#     Select_Advertiser_Name = models.CharField(max_length=200)
#     resp = requests.get('http://api.mobidiscover.affise.com/3.0/partner/offers?API-Key=f12291b89f779461e5425ed922a837e0b2dbc079')
#     data = resp.content
#     JSONFORMAT = json.loads(data)
#     OFFERDATA = JSONFORMAT['offers']
#     #i=1
#     for OFFER1 in OFFERDATA:
#
#     #    print OFFERDATA[i]
#
#         # print "Offer Number:" + str(i)
#         # OFFER_TITLE = OFFER1['title'].encode("utf-8")
#         # print "Title: " + str(OFFER_TITLE)
#         # print "Preview Link: " + OFFER1['preview_url']
#         # print "Tracking Link: " + OFFER1['links'][0]['url']
#         # OFFER_DESCRIPTION = OFFER1['description'].encode("utf-8")
#         # print "Description: " + str(OFFER_DESCRIPTION)
#         # print "Logo URL:" + OFFER1['logo']
#         # Revenue_amt = OFFER1['payments'][0]['revenue']
#         # print "Revenue: " + str(Revenue_amt)
#         # print "OfferID: " + OFFER1['offer_id']
#         # i=i+1
#         browser = "http://api.mobidiscover.affise.com/3.0/admin/offer"
#         headers = {"API-key": "a0f9732f9438aaae0913176015affa67527af607"}
#         data = {'title' : OFFER1['title'].encode("utf-8"),
#                 'advertiser' : '5a4b1758c101d52b008b488a',
#                 'url' : OFFER1['links'][0]['url'],
#                 'url_preview' : OFFER1['preview_url'],
#                 'description' : OFFER1['description'].encode("utf-8"),
#                 'status' : 'suspended',
#                 'freshness' : 'exclusive' ,
#                 'privacy' : 'private'}
#         response = requests.post(browser, headers = headers, data = data)
#         class Meta:
#             verbose_name_plural = "MANUAL API CALL"
