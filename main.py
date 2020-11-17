from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import time

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

Account = 'xxx'
passkey = 'xxx'

url1 = "http://6.6.6.6/"

r = requests.get(url1,headers={"Content-Type":"application/json"},allow_redirects=True)

pattern = re.compile("href=['\"]([^\"'>]*?)['\"].*?",re.S)

url2 = re.search(pattern,r.text).group(1)

#print(url2)

driver.get(url2)
#driver.maximize_window()
input_first = driver.find_elements_by_class_name("edit_lobo_cell")
#input_second = driver.find_element_by_name("upass")
#click_1 = driver.find_element_by_name("0MKKey")

#print(input_first[0].id)
#print(input_first[1].id)
#print(input_first[2].id)
#print(input_first[3].id)
#print(input_first[4].id)
#print(input_second)
#time.sleep(1)

input_first[3].send_keys(Account)
input_first[4].send_keys(passkey)
input_first[2].click()

driver.quit()