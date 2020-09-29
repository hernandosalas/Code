import requests
from lxml.html import fromstring

import requests
from itertools import cycle
import traceback

import requests   
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from lxml import etree, html
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import time
import sys

from random import randint

# def get_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     proxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             proxies.add(proxy)
#     return proxies

# proxies = get_proxies()
# print(proxies)


# def get_proxies2():
#     driver = webdriver.Chrome(executable_path="chromedriver.exe")
#     driver.get("https://free-proxy-list.net/")
#     time.sleep(5)

#     PROXIES = []
#     proxies = driver.find_elements_by_css_selector("tr[role='row']")
#     for p in proxies:
#         result = p.text.split(" ")

#         if result[-1] == "yes":
#             PROXIES.append(result[0]+":"+result[1])

#     driver.close()
#     print(PROXIES)
#     return PROXIES

# get_proxies2()


# def get_proxies3():
#     driver = webdriver.Chrome(executable_path="chromedriver.exe")
#     url = "https://free-proxy-list.net/"
#     driver.get(url)
#     proxies = []
#     proxy_table = driver.find_elements_by_xpath('//*[@id="proxylisttable"]/tbody/tr')
#     for x in proxy_table:
#         row_data = x.find_elements_by_tag_name('td')
#         proxy = row_data[0].text+":"+row_data[1].text
#         proxies.append(proxy)
#     return set(proxies)

# print (get_proxies3())



# proxies = get_proxies3()
# proxies = {'103.57.143.246:61148', '197.155.80.135:80', '103.57.143.246:61148', '197.155.80.135:80', '164.100.130.128:8080', '88.198.24.108:8080', '103.87.207.188:48792', '197.155.80.137:80', '45.33.99.194:8888', '124.41.213.201:39272',}

# {'103.57.143.246:61148', '197.155.80.135:80', '164.100.130.128:8080', '88.198.24.108:8080', '103.87.207.188:48792', '197.155.80.137:80', '45.33.99.194:8888', '124.41.213.201:39272', '91.203.224.177:36731', '45.127.246.198:8080', '103.214.54.90:8080', '88.99.149.188:31288', '41.215.34.210:80', '113.53.91.12:53281', '94.74.165.210:8080', '182.53.206.47:47592', '139.59.1.14:3128', '178.169.198.238:8080', '170.238.255.90:31113', '197.155.80.147:80'}


def setup_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")
    chrome_options.add_argument("referrer=https://google.com")
    proxies = ['164.100.130.128:8080']
    PROXY = proxies[randint(0, len(proxies)-1)]
    chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
    return driver

driver = setup_chrome_driver()
url="https://httpbin.org/ip"
driver.get(url)
time.sleep(10)


# for proxy in proxies:
#     PROXY = proxy
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     options.add_argument('--proxy-server=http://%s' % PROXY)
#     driver = webdriver.Chrome(options=options)
#     url="https://whatismyipaddress.com/"
#     driver.get(url)
#     time.sleep(10)
#     #Mostly free proxies will get proxy server errors.
#     driver.close()







# #If you are copy pasting proxy ips, put in the list below
# #proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']
# proxies = get_proxies3()
# proxy_pool = cycle(proxies)

# url = 'https://httpbin.org/ip'
# for i in range(1,11):
#     #Get a proxy from the pool
#     proxy = next(proxy_pool)
#     print("Request #%d"%i)
#     try:
#         response = requests.get(url,proxies={"http": proxy, "https": proxy})
#         print(response.json())
#     except:
#         #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
#         #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
#         print("Skipping. Connnection error")