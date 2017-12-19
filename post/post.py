import requests

url = 'http://127.0.0.1/Desktop/'
# data = {
# 	'name': 'nginx'
# }
files = {'file': open("test.txt", 'rb')}
response = requests.post(url = url, files = files)