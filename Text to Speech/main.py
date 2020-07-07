'''
Text to Speech

pip install gtts
pip install playsound
'''


import os
from gtts import gTTS
from playsound import playsound
import time


def speak(temp):
    voice = gTTS(text=temp, lang="en")
    voice.save("temp.mp3")
    print("Speaking.....")
    playsound('temp.mp3')
    time.sleep(2)
    os.remove("temp.mp3")

speak("How are you doing today Carolina?")
