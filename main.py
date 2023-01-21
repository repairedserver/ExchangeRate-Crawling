from bs4 import BeautifulSoup as bs
import requests as req

url = 'https://finance.naver.com/marketindex/exchangeList.naver'
a = req.get(url)
soup = bs(a.text, "html.parser")
tds = soup.find_all('td')

'''
name = []
price = []

for td in tds:
    if len(td.find_all('a')) == 0:
        continue
    name.append(td.get_text(strip=True))

for td in tds:
    if "class"in td.attrs:
        if "sale" in td.attrs["class"]:
            price.append(td.get_text(strip=True))

print(name)
print(price)
'''

name = []
price = []
for td in soup.select('td.tit'):
    name.append(td.get_text(strip=True))
for td in soup.select('td.sale'):
    price.append(td.get_text(strip=True))
print(name)
print(price)
