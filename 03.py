import requests
from bs4 import BeautifulSoup

url = input("Please enter a url: ")

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    bs = BeautifulSoup(html, 'html.parser')

    storage = open('source_code.txt', 'wb')
    storage.write(bs.prettify().encode('utf-8'))
    storage.close()
    title = bs.title.text.encode('utf-8')
    print("Page Exists with title {}".format(title))
else:
    print("Page is not exist!")
