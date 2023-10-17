import requests
import json
from os import system
import webbrowser
import pyttsx3 as pyttsx
import speech_recognition as sr

isDashboard = False
listenForCommand = False
def listen():
    r = sr.Recognizer()
    speach=""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        #await audio
    try:
        speach=r.recognize_google(audio).lower()
    #l= Listening.listening_function()
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service;{0}".format(e))

    except Exception as e:
        print(e)

    return speach
def speak(test):
    speech_engine = pyttsx.init()
    voices = speech_engine.getProperty('voices')
    besedilo=test
    speech_engine.setProperty('rate',150)
    speech_engine.setProperty('voice',voices[14].id)
    speech_engine.setProperty('pitch', 0.8)
    speech_engine.say(besedilo)
    speech_engine.runAndWait()

if (isDashboard):
    webbrowser.open_new('http://192.168.64.55:8000/dashboard')
command = listen()
resPost = requests.post('http://192.168.64.55:1234/sendCommand', params = {'command' : command})

if (listenForCommand):
    speak(json.loads(resPost.content.decode())['answer'])

if ("JAMES" in upper(command)):
    listenForCommand = True