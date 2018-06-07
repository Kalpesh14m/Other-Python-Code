from gtts import gTTS
import time
import os
import random
import pyglet
# pyglet.lib.load_library('avbin0')
# pyglet.have_avbin = True

def tts(text, lang):
    file = gTTS(text= text, lang=lang)
    fileName = '/Users/rohitverma/Desktop/Code_Python_New/Demo/Audio/temp.mp3'
    file.save(fileName)

    # music = pyglet.media.load(fileName, streaming= False)

    # music.play()
    # time.sleep(music.duration)
    os.system("mpg321 " + fileName)
    # os.remove(fileName)
