# pip install requests

#method 1
import urllib.request
from urllib.request import Request, urlopenreq = Request('https://medium.com/@pythonians', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).getcode()
print(webpage)  # 200

# method 2
import requests
r = requests.get("https://medium.com/@pythonians")
print(r.status_code) # 200
