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
    chrome_options.add_argument("user-agent="+str(random.choice(user_agent_list)))
    # chrome_options.add_argument("referrer=https://ecorp.azcc.gov")
    # ADD PROXY
    # proxies = ['165.22.81.30:42685']
    # PROXY = proxies[randint(0, len(proxies)-1)]
    # print(f"Proxy: {PROXY}")
    # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
    return driver

def search_entity_name(searchName):
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
            driver.get('https://ecorp.azcc.gov/PublicBusinessSearch/PublicBusinessInfo?entityNumber='+ entity_id)
            time.sleep(2)
            name = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]').text
            address = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[4]').text
            print(f"Name: {name} / Address: {address}")
            # Back to search from result
            driver.find_element_by_xpath('//*[@id="btnDashboard"]').click()
            # //*[@id="btnDashboard"]
            # driver.find_element_by_xpath('//*[@id="btn_search"]').click()
        except:
            entity_id = "No search results were found"
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="btnReset"]').click()
    except:
        pass
        # print("BOT DETECTED")
        entity_id = "BOT DETECTED"
        # sys.exit("BOT DETECTED")
    return str(entity_id)

def get_entity_information(searchName):
    name = ""
    address = ""
    entity_id = search_entity_name(searchName)
    url = ""
    if entity_id == "BOT DETECTED":
        name = "BOT DETECTED"
        address = "BOT DETECTED"
        url = "BOT DETECTED"
        print(f"url: {url}")
        print(f"name: {name}")
        print(f"address: {address}")
        print()
        return name,address,url
    elif entity_id == "No search results were found":
        name = "No search results were found"
        address = "No search results were found"
        url = "No search results were found"
        print(f"url: {url}")
        print(f"name: {name}")
        print(f"address: {address}")
        print()
        return name,address,url
    elif entity_id != "":
        url = 'https://ecorp.azcc.gov/PublicBusinessSearch/PublicBusinessInfo?entityNumber='+ entity_id
        cookies = {'privacy-policy': '1,XXXXXXXXXXXXXXXXXXXXXX'}
        # headers = {'User-Agent': 'Mozilla/5.0'}
        headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                        "Accept-Encoding": "gzip, deflate", 
                        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
                        "Dnt": "1", 
                        "referrer": 'https://google.com', 
                        "Upgrade-Insecure-Requests": "1", 
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36", 
                        "X-Amzn-Trace-Id": "Root=1-5ee7bae0-82260c065baf5ad7f0b3a3e3"
                }
        time.sleep(randint(3, 7))
        response = requests.get(url, cookies=cookies, headers=headers)
        tree = html.fromstring(response.content)
        try:
            if (tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]')):
                name = tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]')[0].text
                address = tree.xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[4]')[0].text
            else:
                name = "No records to view"
                address = "No records to view"
            print(f"entity_id: {entity_id}")
            print(f"url: {url}")
            print(f"name: {name}")
            print(f"address: {address}")
            print()
        except:
            pass

    return name,address,url

driver = setup_chrome_driver()
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# print(get_entity_information("CENTER FOR ALTERNATIVE MEDICIN"))
print(get_entity_information("CENTER FOR ALTERNATIVE MEDICIN"))

