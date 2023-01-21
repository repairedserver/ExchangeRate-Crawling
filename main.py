import requests as req
import re

url = 'https://finance.naver.com/marketindex/'
res = req.get(url)
cost = res.text

r = re.compile(r'h_lst.*?blind">(.*?)</span>.*?value">(.*?)</', re.DOTALL)
cost = r.findall(cost)
print('-------환율 계산기-------\n')

for i in cost:
    print(i[0], ":", i[1] + '원')
print()