import requests
import json
from os import system
import webbrowser
import pyttsx3 as pyttsx

def speak(test):
    speech_engine = pyttsx.init()
    voices = speech_engine.getProperty('voices')
    besedilo=test
    speech_engine.setProperty('rate',150)
    speech_engine.setProperty('voice',voices[14].id)
    speech_engine.setProperty('pitch', 0.8)
    speech_engine.say(besedilo)
    speech_engine.runAndWait()

webbrowser.open_new('http://192.168.64.55:8000/dashboard')

resPost = requests.post('http://192.168.64.55:1234/sendCommand', params = {'command' : 'Whos is BIll Gates'})
print (json.loads(resPost.content.decode())['answer'])

speak(json.loads(resPost.content.decode())['answer'])
#system("say "+json.loads(resPost.content.decode())['answer'])