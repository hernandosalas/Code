'''
Text to Speech

pip install gtts
pip install playsound
pip install SpeechRecognition
pip install ffmpeg
pip install pydub
pip install pyaudio
pip install watson-developer-cloud
pip install --upgrade "ibm-watson>=4.5.0"
pip install python-dotenv

Unofficial Windows Binaries for Python Extension Packages
https://www.lfd.uci.edu/~gohlke/pythonlibs/
'''

import os
import time
import shutil
import json
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.silence import split_on_silence
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Text to speech
def speak(text,filenameSave):
    voice = gTTS(text=text, lang="en" , slow=False)
    voice.save(filenameSave)

def convertMP3toWAV(mp3filename,outputfilename):
    sound = AudioSegment.from_mp3(mp3filename)
    sound.export(outputfilename, format="wav")

def transcribe_audio_with_watson(path_to_audio_file):
    authenticator = IAMAuthenticator(os.getenv('SPEECH_TO_TEXT_APIKEY'))
    speech_to_text = SpeechToTextV1(
        authenticator=authenticator
    )
    speech_to_text.set_service_url(os.getenv(SPEECH_TO_TEXT_URL))

    with open(join(dirname(__file__), path_to_audio_file), 'rb') as audio_file:
        response = speech_to_text.recognize(audio_file, content_type='audio/wav', model='en-US_NarrowbandModel').get_result()
        return response['results'][0]['alternatives'][0]['transcript']


def prettyPrintJson(filename):
    import pprint
    with open(filename, "r") as read_file:
        my_dict = json.load(read_file)
        pprint.pprint(my_dict)


# prettyPrintJson("test.json")


# Google recognize
def recognize_speech_from_file(audioFilename):
    r = sr.Recognizer()
    with sr.AudioFile(audioFilename) as source:
        # Adjust ambient noise
        r.adjust_for_ambient_noise(source)
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)

    try: 
        print("The audio file contains: " + text) 
    
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
    
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    # exporting the result 
    with open('test.txt',mode ='w') as file: 
        file.write("Recognized text:") 
        file.write("\n") 
        file.write(text) 

# recognize_speech_from_file("temp.wav")

# Google recognize large file
# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    r = sr.Recognizer()

    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                # print(chunk_filename, ":", text)
                whole_text += text

    # Delete audio-chunks folder
    shutil.rmtree('audio-chunks')
    # return the text for all chunks detected
    return whole_text

# print(get_large_audio_transcription("temp.wav"))

# Recognize from mic with google
def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        print("--Start Recording--")
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #   update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def findMicrophoneId():
    mic = sr.Microphone()
    mic_list = sr.Microphone.list_microphone_names()
    for i in mic_list:
        if i == "Remote Audio":
            device_id = mic_list.index(i)
    return device_id

# mic = sr.Microphone(device_index=findMicrophoneId())

# print(recognize_speech_from_mic(sr.Recognizer(),mic))

if __name__ == "__main__":
    load_dotenv()
    filenameSaveMP3 = "temp.mp3"
    filenameSaveWAV = "temp.wav"
    try:
        os.remove(filenameSaveMP3)
        os.remove(filenameSaveWAV)
    except:
        pass
    speak("How are you today?",filenameSaveMP3)
    convertMP3toWAV(filenameSaveMP3,filenameSaveWAV)
    playsound(filenameSaveWAV)
    x = input('Continue with transcription?')
    print(f"What I heard: {transcribe_audio_with_watson(filenameSaveWAV)}")