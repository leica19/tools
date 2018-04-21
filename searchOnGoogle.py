import requests, sys, webbrowser, bs4

GOOGLE_DOMAIN = 'http://google.com/'

print('goo...')

res = requests.get(GOOGLE_DOMAIN + 'search?q=' + ''.join(sys.argv[1:]))

print(res)

soup = bs4.BeautifulSoup(res.text, 'lxml')

elems = soup.select('.r a')

print(elems)

num_open = min(10, len(elems))

for i in range(num_open):
    webbrowser.open(GOOGLE_DOMAIN + elems[i].get('href'))
