# coding: utf-8

import requests, os, re
from bs4 import BeautifulSoup

# Configuration
storagePath = "images/"

checkeditems = 0
checkedimages = []

def get_image(urls):
    global checkedimages, checkeditems
    for url in urls:
        tempurl = url.get('src')
        if not (tempurl.startswith('http') or tempurl.startswith('https')):
            tempurl = 'http://safirmall.com' + tempurl
        if tempurl not in checkedimages:
            checkedimages.append(tempurl)
            try:
                filename = os.path.basename(tempurl)  # http://safirmall.com/logo.svg => logo.svg
                save_path = storagePath + filename
                response = requests.get(tempurl)
                if response.status_code == 200:
                    with open(save_path, 'wb') as f:
                        f.write(response.content)
                        checkeditems += 1
                        print("[+] Image {} saved with {} name".format(checkeditems, filename))
            except:
                print("[-] Problem in save image {}".format(tempurl))
        else:
            print("[-] Image Saved Before..")
    return True

def check(url):
    try:
        target_html = requests.get(url)
        parsed_html = BeautifulSoup(target_html.text, 'html.parser')
        print("[+] Collecting images page : " + parsed_html.title.text)
        images = parsed_html.findAll('img', {'src': re.compile(r'(jpe?g)|(png)$')})
        get_image(images)
    except:
        g=1
    return "[+] All images saved successfully!"

def main():
    url = 'http://safirmall.com/1_fa_0_sitemap.xml'
    data = requests.get(url).text
    bs = BeautifulSoup(data, 'html.parser')
    urls = bs.find_all('url')
    for url in urls:
        print(check(url.loc.text))

if __name__ == "__main__":
    main()