
import requests
import re

url = input("Please enter a url: ")

response = requests.get(url)
regex_pattern = re.compile("<title>(.+?)</title>")

if response.status_code == 200:
    html = response.text
    title = regex_pattern.findall(html)[0].encode('utf-8')

    storage = open('title.txt', 'wb')
    storage.write(title)
    storage.close()

    print("Page Exists with title {}".format(title))

else:
    print("Page is not exist!")
