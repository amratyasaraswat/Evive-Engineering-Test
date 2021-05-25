import requests

localHost = "http://127.0.0.1:5000/"

response = requests.get(localHost + "Lunch ")

print (response.text)