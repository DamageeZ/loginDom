from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

url1 = "http://6.6.6.6/"

r = requests.get(url1,headers={"Content-Type":"application/json"},allow_redirects=True)

pattern = re.compile("href=['\"]([^\"'>]*?)['\"].*?",re.S)

url2 = re.search(pattern,r.text)

print(url2.group(1))


