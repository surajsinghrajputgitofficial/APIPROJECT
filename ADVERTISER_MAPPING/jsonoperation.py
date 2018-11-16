# import requests
# import json
#
# resp = requests.get('http://api.mobidiscover.affise.com/3.0/partner/offers?API-Key=f12291b89f779461e5425ed922a837e0b2dbc079')
# data = resp.content
# JSONFORMAT = json.loads(data)
# OFFERDATA = JSONFORMAT['offers']
# i=1
# for OFFER1 in OFFERDATA:
#
# #    print OFFERDATA[i]
#
#     print "Offer Number:" + str(i)
#     print "Title: " + OFFER1['title'].encode("utf-8")
#     print "Preview Link: " + OFFER1['preview_url']
#     print "Tracking Link: " + OFFER1['links'][0]['url']
#     print "Description: " + OFFER1['description'].encode("utf-8")
#     print "Logo URL:" + OFFER1['logo']
#     Revenue_amt = OFFER1['payments'][0]['revenue']
#     print "Revenue: " + str(Revenue_amt)
#     print "OfferID: " + OFFER1['offer_id']
#     i=i+1
#     browser = "http://api.mobidiscover.affise.com/3.0/admin/offer"
#     headers = {"API-key": "a0f9732f9438aaae0913176015affa67527af607"}
#     data = {'title' : OFFER1['title'].encode("utf-8"),
#             'advertiser' : '5a4b1758c101d52b008b488a',
#             'url' : OFFER1['links'][0]['url'],
#             'url_preview' : OFFER1['preview_url'],
#             'description' : OFFER1['description'].encode("utf-8"),
#             'status' : 'suspended',
#             'freshness' : 'exclusive' ,
#             'privacy' : 'private'}
#     response = requests.post(browser, headers = headers, data = data)
#
# #    print "Creatives" + OFFER1['creatives'][0]['url']
#
# #    print resp
# #print resp.content
# #print OFFERDATA[0]
# #OFFER1 = OFFERDATA[0]
# #print "Title: " + OFFER1['title'].encode("utf-8")
# #print "Preview Link: " + OFFER1['preview_url']
# #print "Tracking Link: " + OFFER1['links'][0]['url']
# #print "Description: " + OFFER1['description']
# #print "Logo URL:" + OFFER1['logo']
# #Revenue_amt = OFFER1['payments'][0]['revenue']
# #print "Revenue: " + str(Revenue_amt)
# #print "OfferID: " + OFFER1['offer_id']
# #print "Creatives" + OFFER1['creatives'][0]['url']


# from datetime import datetime
# import time
# start_time = datetime.now().replace(microsecond=0)
# print "Start Time Was: " + str(start_time)
# end_time = datetime.now().replace(microsecond=0)
# print "End Time Was: " + str(end_time)
# diff = end_time - start_time
# print "Time Difference: " + str(diff)
