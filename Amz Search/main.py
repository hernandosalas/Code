'''
forklift.net scrapper
'''

import requests   
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from lxml import etree, html
import pandas as pd

def getInfoWithBS4(url):
    global df      
  
    cookies = {'privacy-policy': '1,XXXXXXXXXXXXXXXXXXXXXX'}
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, cookies=cookies, headers=headers)
    tree = html.fromstring(response.content)

    print()

    product_title,new_price,old_price = "","",""

    try:
        product_title = tree.xpath('//*[@id="page-content-wrapper"]/section/div/div[2]/div[1]/div[2]/h5/a')[0].text
        product_title = product_title[1:-1]
        print(f"Product Name: {product_title}")
    except :
        pass
    
    try:
        new_price = tree.xpath('//*[@id="page-content-wrapper"]/section/div/div[2]/div[1]/div[2]/div[1]/div[1]/h5/div[1]/span[1]')[0].text
        print(f"New Price: {new_price}")
    except :
        pass  

    try:
        new_price = tree.xpath('//*[@id="page-content-wrapper"]/section/div/div[2]/div[1]/div[2]/div[2]/div[1]/h5/div[1]/span[1]')[0].text
        print(f"New Price: {new_price}")
    except :
        pass  

    try:
        used_price = tree.xpath('//*[@id="page-content-wrapper"]/section/div/div[2]/div[1]/div[2]/div[1]/div[1]/h5/div[2]/span[1]')[0].text
        print(f"Used Price: {used_price}")
    except :
        pass 

    try:
        used_price = tree.xpath('//*[@id="page-content-wrapper"]/section/div/div[2]/div[1]/div[2]/div[2]/div[1]/h5/div[2]/span[1]')[0].text
        print(f"Used Price: {used_price}")
    except :
        pass 

    data = pd.DataFrame([[product_title,new_price,used_price]],columns=['Product','New Price','Used Price'])
    df = df.append(data)



search_item = "gtx+super"
url = 'https://theforklift.net/items?search='+ search_item
cookies = {'privacy-policy': '1,XXXXXXXXXXXXXXXXXXXXXX'}
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, cookies=cookies, headers=headers)
mySoup = soup(response.text, 'html.parser')

# Get all urls
urls = []
for a in mySoup.find_all('a', class_="card-link"):
    urls.append(a['href'])

df = pd.DataFrame()

for urlLink in urls:
    getInfoWithBS4(urlLink)

print(df)
df.to_csv('results.csv', index=False)