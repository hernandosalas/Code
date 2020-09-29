from PyPDF2 import PdfFileReader
import csv
import pandas as pd
import glob, os
import sys 

import requests   
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from lxml import etree, html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from random import randint
import random

import chromedriver_autoinstaller

total_records = 0

def get_chromedriver_path():
    chromedriver_path = ""
    chromedriver_exe = 'chromedriver.exe'
    if os.path.isdir(os.getcwd()+'\\84'):
        chromedriver_path = os.getcwd()+'\\84\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\85'):
        chromedriver_path = os.getcwd()+'\\85\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\86'):
        chromedriver_path = os.getcwd()+'\\86\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\87'):
        chromedriver_path = os.getcwd()+'\\87\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\88'):
        chromedriver_path = os.getcwd()+'\\88\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\89'):
        chromedriver_path = os.getcwd()+'\\89\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\90'):
        chromedriver_path = os.getcwd()+'\\90\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\91'):
        chromedriver_path = os.getcwd()+'\\91\\' + chromedriver_exe
    elif os.path.isdir(os.getcwd()+'\\92'):
        chromedriver_path = os.getcwd()+'\\92\\' + chromedriver_exe
    return chromedriver_path

def setup_chrome_driver(chromedriver_path):
    time.sleep(5)
    # # LAUNCH TOR
    # try:
    #     os.system("taskkill /f /im  tor.exe")
    # except:
    #     pass
    # torexe = os.popen(r'C:\Users\herna_000\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    # time.sleep(5)

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("start-minimized")
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
    # PROXY = "socks5://localhost:9050" # IP:PORT or HOST:PORT
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)

    # ADD PROXY
    # proxies = ['165.22.81.30:42685']
    # PROXY = proxies[randint(0, len(proxies)-1)]
    # print(f"Proxy: {PROXY}")
    # chrome_options.add_argument('--proxy-server=http://%s' % PROXY)

    # driver = webdriver.Chrome(options=chrome_options,executable_path="chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options,executable_path=chromedriver_path)
    driver.minimize_window()
    # show_headers(user_agent)
    show_ip()
    return driver

def get_entity_information(searchName):
    delay = 0.5
    delay_initial = 1.5
    name = ""
    address = ""
    url = ""
    entity_id = ""
    print(f"Search Name: {searchName}")   
    driver.get("https://ecorp.azcc.gov/EntitySearch/Index")
    try:
        # time.sleep(randint(3, 5))
        time.sleep(delay_initial)
        driver.find_element_by_xpath('//*[@id="btnReset"]').click()
        driver.find_element_by_xpath('//*[@id="quickSearch_BusinessName"]').click()
        input = driver.find_element_by_xpath('//*[@id="quickSearch_BusinessName"]')
        input.send_keys(searchName)
        input.send_keys(Keys.ENTER)
        # time.sleep(randint(3, 5))
        time.sleep(delay_initial)
        try:
            entity_id = driver.find_element_by_xpath('//*[@id="grid_resutList"]/tbody/tr/td[1]').text
            time.sleep(delay)
            url = 'https://ecorp.azcc.gov/PublicBusinessSearch/PublicBusinessInfo?entityNumber='+ entity_id
            driver.get(url)
            time.sleep(delay)
            try:
                name = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[2]').text
                address = driver.find_element_by_xpath('//*[@id="grid_principalList"]/tbody/tr[1]/td[4]').text
            except:
                name = "No records to view"
                address = "No records to view"
            time.sleep(delay)
            # Back to search from result
            driver.get("https://ecorp.azcc.gov/EntitySearch/Index")
        except:
            entity_id = "No search results were found"
            time.sleep(delay)
            driver.find_element_by_xpath('/html/body/div[4]/div[7]/div/button').click()
            time.sleep(delay)
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
    print(name,address,url,entity_id)
    print()
    return name,address,url,entity_id

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






def write_csv(input,page_num):
    with open(path[:-4]+'_'+str(page_num)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input])

def extract_text_from_pdf(generate_csv):
    global total_records
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        print("Number of pages found: ",pdf.getNumPages())
        print()

        business = {
            'License Number': [],
            'Business Name': [],
            'Owner Name': [],
            'License Type': [],
            'Service Address': [],
            'Mailing Address': [],
            'Issue Date': [],
            'Principal Information Name': [],
            'Principal Information Address': [],
            'url': [],
            'Entity ID': [],
        }

        for i in range(pdf.getNumPages()):
            page_num = i
            page = pdf.getPage(page_num)
            text = page.extractText()
            textList = text.splitlines()

            if generate_csv:
                write_csv(text,page_num)

            i = 11
            records = 0

            while i < len(textList)-9:
                # print(i,textList[i])

                # Service Address 3 lines / Mailing Address Same Address
                if len(textList[i])==7 and (textList[i+9][0:3]=="113") and (textList[i+6] == "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 3 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+8])
                    business['Mailing Address'].append(textList[i+6])
                    business['Issue Date'].append(textList[i+7])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)


                # Service Address 2 lines / Mailing Address 2 lines
                elif len(textList[i])==7 and (textList[i+9][0:3]=="113") and (textList[i+6] != "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 2 lines / Mailing Address 2 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5] + " " + textList[i+8])
                    business['Issue Date'].append(textList[i+6])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)

                # Last Record / Service Address 2 lines / Mailing Address Same Address
                elif len(textList[i])==7 and (textList[i+8][0:4]=="Page"):
                    print(f"Last Record / Service Address 2 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5])
                    business['Issue Date'].append(textList[i+6])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)
                    break

                # Last Record / Service Address 2 lines / Mailing Address 2 lines
                elif len(textList[i])==7 and (textList[i+9][0:4]=="Page"):
                    print(f"Last Record / Service Address 2 lines / Mailing Address 2 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5] + " " + textList[i+8])
                    business['Issue Date'].append(textList[i+6])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)
                    break

                # Service Address 2 lines / Mailing Address Same Address
                elif len(textList[i])==7 and (textList[i+8][0:3]=="113") and (textList[i+5] == "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 2 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5])
                    business['Issue Date'].append(textList[i+6])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)

                # Service Address 3 lines / Mailing Address 2 lines and 1 middle empty line
                elif len(textList[i])==7 and (textList[i+10][0:3]=="113"):
                    print(f"Service Address 3 lines / Mailing Address 2 lines and 1 middle empty line - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+8])
                    business['Mailing Address'].append(textList[i+6] + " " + textList[i+9])
                    business['Issue Date'].append(textList[i+7])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)

                # Service Address 3 lines / Mailing Address 3 lines
                elif len(textList[i])==7 and (textList[i+11][0:3]=="113"):
                    print(f"Service Address 3 lines / Mailing Address 3 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+9])
                    business['Mailing Address'].append(textList[i+6] + " " + textList[i+7] + " " + textList[i+10])
                    business['Issue Date'].append(textList[i+8])
                    name, address, url, entity_id = get_entity_information(textList[i+1])
                    business['Principal Information Name'].append(name)
                    business['Principal Information Address'].append(address)
                    business['url'].append(url)
                    business['Entity ID'].append(entity_id)

                i+=1
        
            print()
            print(f"Number of records in page {page_num}: {records}")
            print()
            total_records += records
            
        df = pd.DataFrame(business, columns = ['License Number','Business Name','Owner Name','License Type','Service Address','Mailing Address','Issue Date','Principal Information Name','Principal Information Address','url','Entity ID'])
        df.to_excel (path[:-4]+'.xlsx', index = False, header=True)

def get_pdfs():
    pdfs_list = []
    os.getcwd()
    for file in glob.glob("*.pdf"):
        pdfs_list.append(file)
    print("Pdf files found: ",pdfs_list)
    print()
    return (pdfs_list)

def get_xlsx():
    xlsx_list = []
    os.getcwd()
    for file in glob.glob("*.xlsx"):
        xlsx_list.append(file)
    # print("xlsx_list: ",xlsx_list)
    return (xlsx_list)

def delete_csv_and_xlsx():    
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.xlsx'):
            os.remove(os.getcwd() + "\\" + file_name)
        elif file_name.endswith('.csv'):
            os.remove(os.getcwd() + "\\" + file_name)

def delete_all_xlsx_except_total():
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.xlsx') and file_name !="total.xlsx":
            os.remove(os.getcwd() + "\\" + file_name)

def join_xlsx():
    df = pd.DataFrame()
    xlsx_list = get_xlsx()
    for file in xlsx_list:
        df = df.append(pd.read_excel(file), ignore_index=True) 
    df.head() 

    # Write xlsx file with auto fit width columns
    writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index = False)
    worksheet = writer.sheets['Sheet1']
    for idx, col in enumerate(df):
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(), len(str(series.name)))) + 2  
        worksheet.set_column(idx, idx, max_len)
    writer.save()

def get_arguments():
    args = []
    for arg in sys.argv:
        args.append(arg)
    if len(args) > 1:
        print("Arguments:")
        print(args[1:])
    print()

# START TIME    
start = time.time()
# PROCESS ALL PDFs IN DIRECTORY
get_arguments()
delete_csv_and_xlsx()
pdfs_list = get_pdfs()
# pdfs_list = ['2020-07-13.pdf']
print("///////////////////////////////////////////////")
print("---Extraction of texts from pdfs - Started")
print("///////////////////////////////////////////////")
print()
for pdf in pdfs_list:
    # CONFIG CHROMEDRIVER
    chromedriver_autoinstaller.install(cwd=True)
    chromedriver_path = get_chromedriver_path()
    driver = setup_chrome_driver(chromedriver_path)
    path = pdf
    print("-----------------------------------------------------------------------------------------------")
    print("Extracting text from pdf: ", path)
    extract_text_from_pdf(generate_csv=False)
    driver.quit()
print()
print("///////////////////////////////////////////////")
print("---Extraction of texts from pdfs - Ended")
print("///////////////////////////////////////////////")
print()
print("***********************************************")
print("Results total.xlsx generated")
print(f"Total records processed: {total_records}")
join_xlsx()
delete_all_xlsx_except_total()

#END TIME
end = time.time()
print(end - start)

