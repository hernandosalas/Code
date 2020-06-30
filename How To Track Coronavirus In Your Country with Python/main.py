'''
Download Chrome Driver
https://chromedriver.chromium.org/
https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_win32.zip

How to hide a password in a Python script with keyring
pip install keyring
import keyring
keyring.set_password("secretKeyring", "secret_username", "secret_password")
keyring.get_password("secretKeyring", "secret_username")
'''

# $ pip install virtualenv
# $ virtualenv --system-site-packages -p python ./venv
# $ .\venv\Scripts\activate
# $ pip install selenium
# $ pip install yagmail

from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_data(self):
        #try:
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')
        country_element = table.find_element_by_xpath("//td[contains(., 'Colombia')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        total_cases = data[1]
        new_cases = data[2]
        total_deaths = data[3]
        new_deaths = data[4]
        active_cases = data[5]
        total_recovered = data[6]
        serious_critical = data[7]

        print("Country: " + country_element.text)
        print("Total cases: " + total_cases)
        print("New cases: " + new_cases)
        print("Total deaths: " + total_deaths)
        print("New deaths: " + new_deaths)
        print("Active cases: " + active_cases)
        print("Total recovered: " + total_recovered)
        print("Serious, critical cases: " + serious_critical)

        print("-----------------SENDING EMAIL---------------------")
        send_mail(country_element.text, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical)

        self.driver.close()
        #except:
        self.driver.quit()

def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
    import yagmail
    import keyring

    sender_email = "hernandosalas@gmail.com"
    receiver_email = "hernandosalas@gmail.com"
    passwordApp = keyring.get_password("secretKeyring", "hernandosalas@gmail.com")
    subject = 'Coronavirus stats in your country today!'

    yag = yagmail.SMTP(user=sender_email, password=passwordApp)

    contents = ['Today in ' + country_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases +'\
        \nNew cases: ' + new_cases + '\
        \nTotal deaths: ' + total_deaths + '\
        \nNew deaths: ' + new_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nSerious, critical cases: ' + serious_critical  + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/']

    yag.send(receiver_email, subject, contents)

bot = Coronavirus()
bot.get_data()
