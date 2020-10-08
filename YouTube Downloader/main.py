'''
Build a YouTube Downloader with Python
https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97

1.Uninstall any previous pytube versions (either pytube/pytube3)
2.Perform a clean start in conda/python environment as "pip install pytube3"
3.Go to the package location of pytube and look for file pytube/extract.py
4.Look for the line "parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)"
5.Change "cipher" ---> "signatureCipher"
'''
# "C:\Users\herna_000\AppData\Local\Programs\Python\Python37\Lib\site-packages"


from pytube import YouTube

link = "https://www.youtube.com/watch?v=1idbbsdqM6Y"
yt = YouTube(link)

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
# print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)
#printing all the available streams
# print(yt.streams)
# printing all audio-only available streams
# print(yt.streams.filter(only_audio=True))
# printing all video-only available streams
# print(yt.streams.filter(only_video=True))

# filter out progressive streams first
print(yt.streams.filter(progressive=True))

# get the highest resolution progressive stream available
ys = yt.streams.get_highest_resolution()

# Choose any stream by the help of its itag
# ys = yt.streams.get_by_itag('18')

#Starting download
print("Downloading...")
path = ""
ys.download(path)
print("Download completed!!")