import requests
from paper import text

url = 'http://127.0.0.1:5000'
myobj = {'text': text}

x = requests.post(url, json = myobj)

print("request sent!")
print(x.text)