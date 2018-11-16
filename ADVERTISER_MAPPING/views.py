# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
import mysql.connector
import json
import sys
from datetime import datetime
from time import time

def getapi(request):
    resp = requests.get('http://api.mobidiscover.affise.com/3.0/partner/offers?API-Key=f12291b89f779461e5425ed922a837e0b2dbc079')
    data = resp.content
    JSONFORMAT = json.loads(data)
    OFFERDATA = JSONFORMAT['offers']
    i=1
    for OFFER1 in OFFERDATA:

    #    print OFFERDATA[i]

        print "Offer Number:" + str(i)
#        print "Title: " + OFFER1['title'].encode("utf-8")
        print "Preview Link: " + OFFER1['preview_url']
        print "Tracking Link: " + OFFER1['links'][0]['url']
#        print "Description: " + OFFER1['description'].encode("utf-8")
        print "Logo URL:" + OFFER1['logo']
        Revenue_amt = OFFER1['payments'][0]['revenue']
        print "Revenue: " + str(Revenue_amt)
        print "OfferID: " + OFFER1['offer_id']
        i=i+1
        browser = "http://api.mobidiscover.affise.com/3.0/admin/offer"
        headers = {"API-key": "a0f9732f9438aaae0913176015affa67527af607"}
        data = {#'title' : OFFER1['title'].encode("utf-8"),
                'advertiser' : '5a4b1758c101d52b008b488a',
                'url' : OFFER1['links'][0]['url'],
                'url_preview' : OFFER1['preview_url'],
                #'description' : OFFER1['description'].encode("utf-8"),
                'status' : 'suspended',
                'freshness' : 'exclusive' ,
                'privacy' : 'private'}
        response = requests.post(browser, headers = headers, data = data)
    return HttpResponse('Offers Upload Has Been Successful')
# Create your views here.
def index(request):
    fun="api"
    html="<form action='%s' method='get'>"%fun
    html=html+"<button type='submit' name='Manual_API_Call' value='API_CALL'>getDate</button></form>"
    return HttpResponse(html)
    #return HttpResponse('<form action=><input type="button" id="insertapi" name="Manual_API_Call" value="Make API Call" onclick='{% url "getapi" %}'>')

#
# from django.http import HttpResponse
import datetime
import time

def current_datetime(request):
    now = datetime.datetime.now()
    #html ="<html><body>It is now  This is another thins <input type='text' value='%s' /></br> </body></html>" %now
    html="<form action='%s'>"%datetime.datetime.now()
    html=html+"<input type='text' value='%s' />"%now
    html=html+"</form>";
    return HttpResponse(html)
def mobidiscover(request):
    html='<head><title>Mobidiscover Digital Media - Online Attandance </title></head><body><center><img src="mobidiscover_logo.png" height="120" width="200"/></center><br><center><b>Mobidiscover Digital Media - Onlince Attandance</b></center></body>'
    return HttpResponse(html)

def show_realtime_time_diff(request):
    start_time = datetime.datetime.now().replace(microsecond=0)
    time.sleep(5)
#    end_time = datetime.datetime.now().replace(microsecond=0)
    time_diff = datetime.datetime.now().replace(microsecond=0) - start_time
    print time_diff
    html = "Start Time: &nbsp;&nbsp;&nbsp;<input type='text' value='%s' />" %start_time
    html = html + "<br>End Time: &nbsp;&nbsp;&nbsp;<input type='text' value='%s' />" % datetime.datetime.now().replace(microsecond=0)
    html = html + "<br>Time Difference: &nbsp;&nbsp;&nbsp;<input type='text' value='%s' />" %time_diff
    return HttpResponse(html)
