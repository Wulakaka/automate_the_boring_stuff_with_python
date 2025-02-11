#! python3
# downloadXkcd.py = Downloads every single XKCD comic.


import os, requests, bs4, logging
from selenium import webdriver
from selenium.webdriver.common.by import By


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
browser = webdriver.Edge()
url = 'https://www.ykmh.net/manhua/huoyingrenzhe/236709.html'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
page = 1
while page <= 20:
    param = '?p=' + str(page)
    # Download the page.
    print('Downloading page %s...' % (url + param))
    browser.get(url + param)
    containerElem = browser.find_element(by=By.ID, value='images')
    if not containerElem:
        print('Could not find image container.')
    else:
        comicElem = containerElem.find_element(by=By.CSS_SELECTOR, value='img')
        if not comicElem:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem.get_dom_attribute('src')
            # Download the image.
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    page += 1

print('Done.')
