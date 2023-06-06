import requests

url = 'http://localhost:8000'
headers = {'Transfer-Encoding': 'chunked'}
data = open('file.txt', 'rb')
response = requests.post(url, headers=headers, data=data)
print(response.content.decode())
