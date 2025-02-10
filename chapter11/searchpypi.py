#! python3
# searchpypi.py - Open several search results.

import requests, sys, webbrowser, bs4, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

print('Searching...')  # display text while downloading the search result page
logging.debug('url is: ' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(res.text[:1250])

# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
logging.debug(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
