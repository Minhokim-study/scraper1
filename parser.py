## parser.py
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()

## HTTP GET request
req = requests.get('https://www.reddit.com/r/CatsOnPizza/', headers={'User-Agent': ua.chrome})

## Get HTML Source code
html = req.text

soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
my_titles = soup.select(
    'div > div > div > a > div > h3'
)

for title in my_titles:
    print(title.text)

'''
## Get HTML Header
header = req.headers
## Get HTTP Satus (200: Normal)
status = req.status_code
## Find HTTP is ok or not
is_ok = req.ok
'''