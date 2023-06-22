import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

link = input('Enter URL: ')
count = int(input('Enter count: ')) 
position = int(input('Enter position: '))


print('Retrieving: ', link)
for i in range(count):
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    cn = 0
    ps = 0

    for tag in tags:
        ps += 1
        if ps == position:
            link = tag.get('href', None)
            print('Retrieving: ', link)
            break