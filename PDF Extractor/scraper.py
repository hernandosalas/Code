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
import random

def setup_chrome_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('log-level=3')

    # USER AGENTS
    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    ]
    user_agent = str(random.choice(user_agent_list))
    chrome_options.add_argument("user-agent="+ user_agent)
    chrome_options.add_argument("referrer=https://ecorp.azcc.gov")

    # SET TOR PROXY
    try:
        os.system("taskkill /f /im  tor.exe")
    except:
        pass
    time.sleep(3)
    torexe = os.popen(r'C:\Users\herna_000\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT
    options = webdriver.ChromeOptions()
    options.add_argument('--proxy-server=%s' % PROXY)

    # ADD PROXY
    # proxies = ['165.22.81.30:42685']
    # PROXY = proxies[randint(0, len(proxies)-1)]
    # print(f"Proxy: {PROXY}")
    # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
    # show_headers(user_agent)
    show_ip()
    return driver

def get_entity_information(searchName):
    name = ""
    address = ""
    url = ""
    entity_id = ""
    print(f"Search Name: {searchName}")   
    driver.get("https://ecorp.azcc.gov/EntitySearch/Index")
    try:
        time.sleep(randint(3, 7))
        driver.find_element_by_xpath('//*[@id="btnReset"]').click()
        driver.find_element_by_xpath('//*[@id="quickSearch_BusinessName"]').click()
        input = driver.find_element_by_xpath('//*[@id="quickSearch_BusinessName"]')
        input.send_keys(searchName)
        input.send_keys(Keys.ENTER)
        time.sleep(randint(3, 7))
        try:
            entity_id = driver.find_element_by_xpath('//*[@id="grid_resutList"]/tbody/tr/td[1]').text
            time.sleep(2)
            url = 'https://ecorp.azcc.gov/PublicBusinessSearch/PublicBusinessInfo?entityNumber='+ entity_id
            driver.get(url)
            time.sleep(2)
            try:
                name = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]').text
                address = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[4]').text
            except:
                name = "No records to view"
                address = "No records to view"
            time.sleep(2)
            # Back to search from result
            driver.get("https://ecorp.azcc.gov/EntitySearch/Index")
        except:
            entity_id = "No search results were found"
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="btnReset"]').click()
            name = "No search results were found"
            address = "No search results were found"
            url = "No search results were found"
    except:
        # print("BOT DETECTED")
        name = "BOT DETECTED"
        address = "BOT DETECTED"
        url = "BOT DETECTED"
        entity_id = "BOT DETECTED"
        # sys.exit("BOT DETECTED")
    print(name,address,url)
    print()
    return name,address,url

def show_headers(user_agent):
    url = 'https://httpbin.org/headers'
    #Set the headers 
    headers = {'User-Agent': user_agent}
    #Make the request
    response = requests.get(url,headers=headers)
    
    print("Request \nUser-Agent Sent:%s\n\nHeaders Recevied by HTTPBin:"%(user_agent))
    print(response.json())
    print("-------------------")

def show_ip():
    url = 'https://httpbin.org/ip'
    print("Request")
    try:
        response = requests.get(url)
        print(response.json())
    except:
        print("Skipping. Connnection error")


# def get_chrome_version():
#     import os
#     stream = os.popen(r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value')
#     output = stream.read()
#     print(output)

# def download_chrome_driver():
#     import urllib.request
#     print('Beginning file download with urllib2...')
#     url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
#     urllib.request.urlretrieve(url, '/Users/scott/Downloads/cat.jpg')





# def get_entity_information(searchName):
#     name = ""
#     address = ""
#     entity_id = search_entity_name(searchName)
#     url = ""
#     if entity_id == "BOT DETECTED":
#         name = "BOT DETECTED"
#         address = "BOT DETECTED"
#         url = "BOT DETECTED"
#         print(f"url: {url}")
#         print(f"name: {name}")
#         print(f"address: {address}")
#         print()
#         return name,address,url
#     elif entity_id == "No search results were found":
#         name = "No search results were found"
#         address = "No search results were found"
#         url = "No search results were found"
#         print(f"url: {url}")
#         print(f"name: {name}")
#         print(f"address: {address}")
#         print()
#         return name,address,url
#     elif entity_id != "":
#         url = 'https://ecorp.azcc.gov/PublicBusinessSearch/PublicBusinessInfo?entityNumber='+ entity_id
#         cookies = {'privacy-policy': '1,XXXXXXXXXXXXXXXXXXXXXX'}
#         # headers = {'User-Agent': 'Mozilla/5.0'}
#         headers = {
#                         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
#                         "Accept-Encoding": "gzip, deflate", 
#                         "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
#                         "Dnt": "1", 
#                         "referrer": 'https://google.com', 
#                         "Upgrade-Insecure-Requests": "1", 
#                         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
#                         "X-Amzn-Trace-Id": "Root=1-5ee7bae0-82260c065baf5ad7f0b3a3e3"
#                 }
#         time.sleep(randint(3, 7))
#         response = requests.get(url, cookies=cookies, headers=headers)
#         tree = html.fromstring(response.content)
#         try:
#             if (tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]')):
#                 name = tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]')[0].text
#                 address = tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[4]')[0].text
#             else:
#                 name = "No records to view"
#                 address = "No records to view"
#             print(f"entity_id: {entity_id}")
#             print(f"url: {url}")
#             print(f"name: {name}")
#             print(f"address: {address}")
#             print()
#         except:
#             pass

#     return name,address,url

driver = setup_chrome_driver()
# time.sleep(3)
# driver.quit()
# try:
#     os.system("taskkill /f /im  tor.exe")
# except:
#     pass
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# print(get_entity_information("CENTER FOR ALTERNATIVE MEDICIN"))
print(get_entity_information("AZURE NAIL AND HAIR STUDIO"))

