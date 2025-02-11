import bs4, requests, os, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def main():
    print('Enter the link: ')
    link = input()
    verifyLink(link)


def verifyLink(link):
    res = requests.get(link)
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if res.status_code == 404:
            print('Not Found')
        else:
            print(f'HTTP error occurred: {e}')
        return
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('a')
    os.makedirs('./links', exist_ok=True)
    for i in range(len(linkElems)):
        l = linkElems[i].get('href')
        if l and l.startswith('http'):
            try:
                res = requests.get(l)
                res.raise_for_status()
                print('Downloading %s...' % (l))
                logging.debug(os.path.basename(l))
                downFile = open(os.path.join('links', 'page%s.html' % i), 'wb')
                for chunk in res.iter_content(100000):
                    downFile.write(chunk)
                downFile.close()
            except requests.exceptions.HTTPError as e:
                if res.status_code == 404:
                    print('Broken link: ' + l)
                else:
                    print(f'HTTP error occurred: {e}')


main()
