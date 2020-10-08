'''
Extracting Speech from Video
https://towardsdatascience.com/extracting-speech-from-video-using-python-f0ec7e312d38

pip install SpeechRecognition moviepy

MP4 (mp4, m4a, m4v, f4v, f4a, m4b, m4r, f4b, mov)
3GP (3gp, 3gp2, 3g2, 3gpp, 3gpp2)
OGG (ogg, oga, ogv, ogx)
WMV (wmv, wma, asf*)

MP3
AAC
WMA
AC3 (Dolby Digital)

'''

import speech_recognition as sr 
import moviepy.editor as mp

clip = mp.VideoFileClip(r"sample.mp4") 
 
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()
audio = sr.AudioFile("converted.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

# exporting the result 
with open('recognized.txt',mode ='w') as file: 
   file.write("Recognized Speech:") 
   file.write("\n") 
   file.write(result) 
   print("ready!")