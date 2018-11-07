import requests

url = input("Please enter a url: ")

response = requests.get(url)
if response.status_code == 200:
    print("Page Exists!")
else:
    print("Page is not exist!")
