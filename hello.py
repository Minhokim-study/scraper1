from bs4 import BeautifulSoup
import urllib.request as urllib2
import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://www.reddit.com')
print (r.status)

redditFile = urllib2.urlopen("http://www.reddit.com")
redditHtml = redditFile.read()
redditFile.close()

soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))