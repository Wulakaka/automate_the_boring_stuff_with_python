import bs4, requests, os, pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By

def main(code):
    # print('Enter code:')
    # code = input()

    url = 'https://www.dy2018.com/i/%s.html' % code
    print('Downloading page %s...' % url)

    driver = webdriver.Edge()
    driver.get(url)

    # res = requests.get(url)
    # try:
    #     res.raise_for_status()
    # except Exception as exc:
    #     print('There was a problem: %s' % (exc))

    # soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # linkElems = soup.select('a[href^="magnet"]')
    linkElems = driver.find_elements(by=By.CSS_SELECTOR, value='a[href^="magnet"]')

    text = ''
    for i in range(len(linkElems)):
        # magnet = linkElems[i].get('href')
        magnet = linkElems[i].get_attribute('href')
        text += magnet + '\n'

    pyperclip.copy(text)
    print('Copied to clipboard: %s' % text)


main('101292')
