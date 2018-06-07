import os
import speech_recognition as sr
from SpeechToText import Camera
from SpeechToText import OpenChrome
from SpeechToText import InputText
import sys

r = sr.Recognizer()

def searchData(text):
    if(str(text) == 'Cemera' or str(text) == 'camera'):
        os.system('say ' + "Thank You, I am Opening " + text)
        Camera.camera()
        me()

    else:
        os.system('say ' + "Thank You, Your Text is " + text)
        me()

def google_search(text):
    os.system('say ' + "Thank You, I am Searching " + text + "on google")
    OpenChrome.OpenChrome(text)


def data(text):
    data = InputText.inputText(text)

    if(str(text) == 'bye' or str(text) == 'bye'):
        sys.exit()
        print("Bye!!!")
    else:
        if(data == 'search' or data == 'Search'):
            google_search(InputText.inpu(text))
        else:
            searchData(text)

def me():
    #user Microphone resource
    with sr.Microphone() as source:
        os.system('say '+ 'Hi, My name is KIM ' + 'What you want to search?')
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        data(text)

    except Exception as e:
        print(e)

while True:
    me()
