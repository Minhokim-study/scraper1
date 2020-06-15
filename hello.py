from bs4 import BeautifulSoup
import urllib.request as urllib2

url = 'https://www.reddit.com/r/CatsOnPizza/'
handle = urllib2.urlopen(url)
data = handle.read()
handle.close()

soup = BeautifulSoup(page.text, 'html.parser')
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))