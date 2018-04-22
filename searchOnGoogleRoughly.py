
import requests, sys, webbrowser, bs4

GOOGLE_DOMAIN = 'http://google.com/'

res = requests.get(GOOGLE_DOMAIN + 'search?q=' + ''.join(sys.argv[1:]))

try:
    if sys.argv[2]:
        tabNum = int(sys.argv[2])
except:
    tabNum = 5

print('goo...')

# print the status code
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
elems = soup.select('.r a')

num_open = min(tabNum, len(elems))
for i in range(num_open):
    webbrowser.open(GOOGLE_DOMAIN + elems[i].get('href'))
