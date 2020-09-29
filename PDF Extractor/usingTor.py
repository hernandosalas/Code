from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

from stem import Signal
from stem.control import Controller

from bs4 import BeautifulSoup

import os


# signal TOR for a new connection
def switchIP():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def my_proxy(PROXY_HOST,PROXY_PORT):
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('log-level=3')

    # ADD PROXY
    print(str(PROXY_HOST+":"+str(PROXY_PORT)))
    PROXY = str
    print(f"Proxy: {PROXY}")
    chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
    return driver


# for x in range(2):
#     proxy = my_proxy("127.0.0.1", 9050)
#     proxy.get("https://whatsmyip.com/")
#     html = proxy.page_source
#     soup = BeautifulSoup(html, 'lxml')
#     print(soup.find("span", {"id": "ipv4"}))
#     print(soup.find("span", {"id": "ipv6"}))
#     switchIP()

# To use Tor's SOCKS proxy server with chrome, include the socks protocol in the scheme with the --proxy-server option
# PROXY = "socks5://127.0.0.1:9150" # IP:PORT or HOST:PORT

import time
import os

try:
    os.system("taskkill /f /im  tor.exe")
except:
    pass
torexe = os.popen(r'C:\Users\herna_000\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
# PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT
PROXY = "198.98.57.133:9001"
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=options,executable_path="chromedriver.exe")
# driver.get("http://check.torproject.org")
# driver.get("https://httpbin.org/ip")
time.sleep(10)
driver.get("http://ecorp.azcc.gov/EntitySearch/Index")
# time.sleep(3)
# driver.quit()
# try:
#     os.system("taskkill /f /im  tor.exe")
# except:
#     pass

# https://www.iplocation.net/find-ip-address







# with Controller.from_port(port = 9050) as controller:
#     controller.authenticate()
#     controller.signal(Signal.NEWNYM)




# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % prox) #sets conncection to your 9150 port aka Tor Network
# driver = webdriver.Chrome(chrome_options=options,executable_path="chromedriver.exe")
# driver.get("http://check.torproject.org")


# import requests   

# with Controller.from_port(port = 9051) as c:
#     c.authenticate()
#     c.signal(Signal.NEWNYM)

# print(requests.get('https://api.ipify.org', proxies=proxies).text)

# import requests
# from stem import Signal
# from stem.control import Controller

# print(requests.get('https://ident.me').text)

# proxies = {
#     'http': 'socks5://127.0.0.1:9050',
#     'https': 'socks5://127.0.0.1:9050'
# }

# print(requests.get('https://ident.me', proxies=proxies).text)

# torexe = os.popen(r'C:\Users\herna_000\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
# with Controller.from_port(port = 9051) as c:
#     c.authenticate()
#     c.signal(Signal.NEWNYM)

# print(requests.get('https://ident.me', proxies=proxies).text)