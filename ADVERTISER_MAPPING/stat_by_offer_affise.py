import requests
import json

APIURL = "http://api.mobidiscover.affise.com/3.0/stats/getbyprogram"
headers = {"API-key": "a0f9732f9438aaae0913176015affa67527af607"}
data = 'filter[date_from]=2018-11-05&filter[date_to]=2018-11-05'
url = APIURL + data
response = requests.get(url, headers = headers)
print response
print response.content
