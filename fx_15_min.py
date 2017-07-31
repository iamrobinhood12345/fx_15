import requests
from bs4 import BeautifulSoup

rates_dict = {}

page = requests.get()
c = page.content
soup = BeautifulSoup(c)
rates = soup.find_all('td', {'class': 'rtRates'})

for each in rates:
    pair = str(each)[42:45] + '/' + str(each)[53:56]
    rate = each.text
    rates_dict[pair] = rate

print(rates_dict)
