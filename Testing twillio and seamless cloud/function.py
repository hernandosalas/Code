"""
By default Seamless Cloud will execute the file `function.py`.
You can override this behaviour by using --entrypoint flag.

Monitor country's COVID situation and decide when it's safe to travel
https://github.com/seamless-io/templates/tree/master/monitor_country_covid_status
"""
import os
from datetime import datetime, timedelta

import requests

from twilio.rest import Client
from dateutil.parser import parse

from configparser import ConfigParser

def read_config():
    config = ConfigParser()
    config.read('config.ini')
    return config.get('main', 'ACCOUNT_SID'),config.get('main', 'AUTH_TOKEN'),config.get('main', 'PHONE_NUMBER')

def get_country_confirmed_infected(country, start_date, end_date):
    resp = requests.get(f"https://api.covid19api.com/country/{country}/status/confirmed",
                        params={"from": start_date,
                                "to": end_date})
    return resp.json()


def send_whatsapp_message(msg):
    account_sid = str(ACCOUNT_SID)  # your Twilio account id
    auth_token = str(AUTH_TOKEN)  # your Twilio auth token
    from_number = 'whatsapp:+14155238886'
    to_number = f'whatsapp:{PHONE_NUMBER}'
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                                from_=from_number,  
                                body=msg,      
                                to= to_number
                            ) 

def main():
    country = "Colombia"
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    print("Getting COVID data")
    cases = get_country_confirmed_infected(country, week_ago, today)
    latest_day = cases[-1]
    earliest_day = cases[0]
    percentage_increase = (latest_day['Cases'] - earliest_day['Cases']) / (earliest_day['Cases'] / 100)
    msg = f"There were {latest_day['Cases']} confirmed COVID cases in {country} " \
          f"on {parse(latest_day['Date']).date()}\n"
    if percentage_increase > 0:
        msg += f"This is {round(abs(percentage_increase), 4)}% increase over the last week. " \
               f"Travel is not recommended."
    else:
        msg += f"This is {round(abs(percentage_increase), 4)}% decrease over the last week. " \
               f"Travel may be OK."
    print("Sending Whatsapp message")
    send_whatsapp_message(msg)
    print("Job finished successfully")


if __name__ == '__main__':
    ACCOUNT_SID,AUTH_TOKEN,PHONE_NUMBER = read_config()
    main()