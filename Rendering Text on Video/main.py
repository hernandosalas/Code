'''
Rendering Text on Video using Python
https://towardsdatascience.com/rendering-text-on-video-using-python-1c006519c0aa

pip install moviepy
choco install imagemagick.app

Sample videos
https://www.learningcontainer.com/mp4-sample-video-files-download/

find your moviepy's catalog, then find the moviepy/config_defaults.py, open this file and add after the last line:
IMAGEMAGICK_BINARY = "C:\\Program Files\\ImageMagick_VERSION\\convert.exe

install legacy checkbox at setup of imagemagick


'''
# C:\Users\herna_000\AppData\Local\Programs\Python\Python37\Lib\site-packages

import moviepy.editor as mp

my_video = mp.VideoFileClip("sample-video.mp4", audio=True)

w,h = moviesize = my_video.size

my_text = mp.TextClip("The Art of Adding Text on Video", font='Amiri-regular', color='white', fontsize=34)

txt_col = my_text.on_color(size=(my_video.w + my_text.w, my_text.h+5), color=(0,0,0), pos=(6,'center'), col_opacity=0.6)

# Animation
txt_mov = txt_col.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )

# Rendering
final = mp.CompositeVideoClip([my_video,txt_mov])

final.subclip(0,17).write_videofile("sample-video.mp4",fps=24,codec='libx264')