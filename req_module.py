import requests


r = requests.get('https://www.makemytrip.com')
print r.url
try:
    print r.text
    print r.content
    print r.json()
except Exception as e:
    print "Exception occured:",e
