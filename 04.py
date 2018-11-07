import requests
from bs4 import BeautifulSoup

url = input("Please enter a url: ")

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    bs = BeautifulSoup(html, 'html.parser')

    print("safirmall cat : ", bs.select('div.image_block > a')[0].img.get('src'))

    for links in bs.find_all('a'):
        print(links['href'])

    logo = bs.find('div', {'id': 'header_logo'}).a.img.get('src')
    if logo.startswith('/'):
        logo = url + logo
    print("safirmall Logo : {}".format(logo))

else:
    print("Page is not exist!")
