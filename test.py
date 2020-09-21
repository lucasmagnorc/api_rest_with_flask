import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/0", {"likes": 10, "name": "Lucas", "views": 100})
print(response.json())
input()
response = requests.get(BASE + "video/0")
print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/0")
print(response.json())
