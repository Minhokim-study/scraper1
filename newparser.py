## newparser.py
import requests
import bs4 as bs
from selenium import webdriver

browser = webdriver.Chrome()
url = ("https://www.samsbeauty.com/service/category/370/Bundle.html")
#req = requests.get('https://www.samsbeauty.com/service/category/370/Bundle.html', headers={'User-Agent': ua.chrome})
browser.get(url)
html = browser.page_source
browser.quit()
#html = req.text
soup = bs.BeautifulSoup(html, 'lxml')
#print (soup.prettify())

my_titles = soup.find("ul", {"class":"productListView viewTySM"}).find_all("p", {"class":"description"})
my_prices = soup.find("ul", {"class":"productListView viewTySM"}).find_all("p", {"class":"price"})

for title in my_titles:
    for price in title:
        print(price.text, end = ' ')
    print()
    #print(soup.find("ul", {"class":"productListView viewTySM"}))
    #print(title.text)


'''
import bs4 as bs
from selenium import webdriver  
browser = webdriver.Chrome()
url = ("http://www.foxsports.com/mlb/scores")
browser.get(url)
html_source = browser.page_source
browser.quit()
soup = bs.BeautifulSoup(html_source, "lxml")
for el in soup.find_all("div", class_="wisbb_name"):
    print(el.get_text())
'''
