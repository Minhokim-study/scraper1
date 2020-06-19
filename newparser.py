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

a = []
b = []
for title in my_titles:
    a.append(title.text)

for price in my_prices:
    b.append(price.text)

c = dict(zip(a, b))
print (c)
    #print(soup.find("ul", {"class":"productListView viewTySM"}))
    #print(title.text)
'''
titles = [row.text for row in my_titles]
prices = [row.text for row in my_prices]
zipped_list = list(zip(titles, prices))
dict_not_list = dict((zip(titles, prices))

print (titles)

for row in zipped_list:
    print(row)

for row in dict_not_list:
    print(row)
'''



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
