import requests
import json
from os import system
import webbrowser
import pyttsx3 as pyttsx

def speak(test):
    speech_engine = pyttsx.init()
    besedilo=test
    speech_engine.say(besedilo)
    speech_engine.runAndWait()

webbrowser.open_new('http://192.168.64.55:8000/dashboard')

resPost = requests.post('http://192.168.64.55:1234/sendCommand', params = {'command' : 'Whos is BIll Gates'})
print (json.loads(resPost.content.decode())['answer'])

speak(json.loads(resPost.content.decode())['answer'])
#system("say "+json.loads(resPost.content.decode())['answer'])