'''

Running ChromeDriver with Python Selenium on Heroku
---------------------------------------------------
Step 1: Download the Buildpacks Necessary for the ChromeDriver

$heroku buildpacks:add --index 1 https://github.com/heroku-buildpack-chromedriver
$heroku buildpacks:add --index 2 https://github.com/heroku-buildpack-chromedriver

Step 2: Add the PATH variable to the Heroku configuration

$heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google_chrome
$heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver

Step 3: The Code

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH
browser = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)


'''



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os


def setup_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument('log-level=3')

    driver = webdriver.Chrome(options=chrome_options,executable_path=os.path.dirname(os.getcwd()) + "\\chromedriver.exe")
    return driver

# Schedule an Appointment
# https://www.miamidade.gov/global/initiatives/coronavirus/schedule-test.page

def main():
    driver = setup_chrome_driver()
    time.sleep(3)
    testing_sites_urls = ["https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTMP","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTTA","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTSD","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTNM","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTOL","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTM2","https://www.miamidade.gov/311direct/#/covid19Testing/MDCOVIDTM1"]

    testing_sites_names = ["Marlins Park","Youth Fairgrounds","South Dade Government Center","North Miami","Opa-locka","Harris Field","Joseph Caleb Center"]

    locations_with_appts_available = 0

    num_of_retries = 1

    for url in range(len(testing_sites_urls)):
        driver.get(testing_sites_urls[url])
        time.sleep(1)
        print()
        print(testing_sites_names[url])

        # Click I understand checkbox
        for i in range(num_of_retries):
            try:
                driver.find_element_by_xpath('//*[@id="main-content"]/ui-view/ui-view/div/div/div/div/div/label/input').click()
                break
            except NoSuchElementException as e:
                time.sleep(1)

        time.sleep(2)

        for i in range(num_of_retries):
            try:
                # Status
                status = driver.find_element_by_xpath('//*[@id="main-content"]/ui-view/ui-view/div/div/div/div[2]/div/div/div/p').text
                # Location Site and Address
                location = driver.find_element_by_xpath('//*[@id="main-content"]/ui-view/ui-view/div/div/div/div[2]/div/div/div[1]').text
                if (status == location):
                    print("No open appointment slots")
                    break
                else:
                    locations_with_appts_available += 1
                    earliest_appt = driver.find_element_by_xpath('//*[@id="main-content"]/ui-view/ui-view/div/div/div/div[2]/div/div/div[2]/p[1]').text
                    print(earliest_appt)
                    print(location)
                    print(testing_sites_urls[url])
                    break
                # Appt available 1
                # print(driver.find_element_by_xpath('//*[@id="main-content"]/ui-view/ui-view/div/div/div/div[2]/div/div/div[2]/p[1]').text)
            except NoSuchElementException as e:
                time.sleep(1)

    print()
    print(f"# of locations with available appts = {locations_with_appts_available}")

main()