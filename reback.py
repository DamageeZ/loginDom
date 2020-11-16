import requests
url = 'http://6.6.6.6/'
r = requests.get(url,headers={"Content-Type":"application/json"},allow_redirects=True)
#print(r.status_code)
print(r.text)