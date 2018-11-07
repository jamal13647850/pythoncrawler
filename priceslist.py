from bs4 import BeautifulSoup
import requests

url = 'http://safirmall.com/1_fa_0_sitemap.xml'
data = requests.get(url).text

bs = BeautifulSoup(data, 'html.parser')

urls = bs.find_all('url')

storage = open('priceslist.txt', 'ab')
for url in urls:
    try:
        pageData = BeautifulSoup(requests.get(url.loc.text).text, 'html.parser')
        product = pageData.select('h1.fontcustom2')[0].text
        price = pageData.select('span#our_price_display')[0].text
        storage.write((product + " \r\n" + price+ " \r\n").encode('utf-8'))
        print(product + " \r\n" +price)
    except:
        price = "0"
        product = ""

storage.close()