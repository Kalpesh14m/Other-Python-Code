"""This Module is for Convert English text into Hindi"""
import speech_recognition as sr
import goslate
from translation import google, ConnectError

r = sr.Recognizer()
gs = goslate.Goslate()


with sr.Microphone() as source:
    print('Say Something:')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print("You said: " + text + '.')

kann = gs.translate(text,'kn')
print(kann)
# print (r.recognize_google(audio))


