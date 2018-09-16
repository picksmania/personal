import requests
import urllib2,urllib

url_address = r'https://www.makemytrip.com/'
payload = { 'inUserName': 'pickssmania08@gmail.com', 'inUserPass': 'rhtdM123' }
with requests.Session() as s:
	p = s.post(url_address, data=payload)
	print p.text
#     # r = s.get('A protected web page url')
# 	# print r.text
# http_proxy  = "http://web-proxy.in.hpecorp.net:8080/"
# https_proxy = "https://web-proxy.in.hpecorp.net:8080/"
# #ftp_proxy   = "ftp://10.10.1.10:3128"
#
# proxyDict = {
#               "http"  : http_proxy,
#               "https" : https_proxy,
#               #"ftp"   : ftp_proxy
#             }
#
# r = requests.get(url_address, proxies=proxyDict)
# r = requests.get('http://www.makemytrip.com', proxies=urllib.getproxies())