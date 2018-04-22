
import requests, sys, webbrowser, bs4

GOOGLE_DOMAIN = 'http://google.com/'
TAB_NUM = 5

print('goo...')

res = requests.get(GOOGLE_DOMAIN + 'search?q=' + ''.join(sys.argv[1:]))

# print the status code
print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')
elems = soup.select('.r a')

num_open = min(TAB_NUM, len(elems))
for i in range(num_open):
    webbrowser.open(GOOGLE_DOMAIN + elems[i].get('href'))
