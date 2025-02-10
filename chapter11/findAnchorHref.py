import requests, bs4

path = 'https://automatetheboringstuff.com/2e/chapter12/'

res = requests.get(path)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
anchorElems = soup.select('a')

for i in range(len(anchorElems)):
    print(anchorElems[i].get('href'))