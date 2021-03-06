from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
from csv import writer


PAGES = [
]

rates_dict = {}
rates_tags = []

for each in PAGES:
    page = get(each)
    c = page.content
    soup = BeautifulSoup(c, 'html.parser')
    for each in soup.find_all('td', {'class': 'rtRates'}):
        pair = str(each)[42:45] + '/' + str(each)[53:56]
        rate = each.text
        rates_dict[pair] = rate

utc_time = datetime.now(timezone('UTC')).strftime("%Y%m%d-%H%M%S")
filename = '/Users/ben/code/finance/fx_15_min/data/' + utc_time + '.csv'

with open(filename, 'w+') as csv_file:
    csv_writer = writer(csv_file)
    for key, value in rates_dict.items():
        csv_writer.writerow([key, value])

print(utc_time)
