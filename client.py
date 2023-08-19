import requests
import json
from os import system

resPost = requests.post('http://192.168.64.119:1234/sendCommand', params = {'command' : 'Whos is BIll Gates'})
print (json.loads(resPost.content.decode())['answer'])

system("say "+json.loads(resPost.content.decode())['answer'])