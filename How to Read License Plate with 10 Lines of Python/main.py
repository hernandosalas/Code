'''
How to Read License Plate with 10 Lines of Python


To start out, you’ll need an OpenALPR account for which you can register
https://www.openalpr.com/
http://doc.openalpr.com/cloud_api.html
https://www.openalpr.com/carcheck-api.html

How to hide a password in a Python script with keyring
pip install keyring

python -i
$import keyring
$keyring.set_password("secretKeyring", "secret_username", "secret_password")
keyring.get_password("secretKeyring", "secret_username")
'''

# $ pip install virtualenv
# $ virtualenv --system-site-packages -p python ./venv
# $ .\venv\Scripts\activate
# $ pip install selenium
# $ pip install yagmail

import requests
import base64
import json
import keyring

def getSecret():
    return keyring.get_password("openalprAPI", "openalprAPI")

def getCarInfo():
    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())


    # Get image url
    # imageURL = "http://plates.openalpr.com/ea7the.jpg"
    # response = requests.get(imageURL)
    # img_base64 = base64.b64encode(response.content)



    url = 'https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url, data = img_base64)

    try:
        print(f"Plate: {r.json()['results'][0]['plate']}")
        print(f"Brand: {r.json()['results'][0]['vehicle']['make'][0]['name']}")
        print(f"Color: {r.json()['results'][0]['vehicle']['color'][0]['name']}")
    except:
        print("Plate cannot be identified")


IMAGE_PATH = "mercedes_car.jpeg"
SECRET_KEY = getSecret()

getCarInfo()