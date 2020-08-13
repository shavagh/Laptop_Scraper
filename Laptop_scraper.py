from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

req = Request("https://www.virginmegastore.ae/en/Electronics-Accessories/Laptops-Tablets/Laptops-Notebooks/c/n010202?q=%3Apage%3D1%26nbResultsPerPage%3D99%26sorting%3DMY_SELECTION%26constraints%3Dcategory%3A8796286320782_%2F_in_stock%3Atrue_%2F_price%3A%5B1000.0%2C1000000.0%29#")
webpage = urlopen(req)
page_html = webpage.read()
webpage.close()

csv_file = open('laptops.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Brand', 'Specifications', 'Price'])

soup = BeautifulSoup(page_html, 'lxml')
ul = soup.find('ul', attrs={'class': 'product-list__item-wrapper g-row__4'})
for laptop in ul.find_all('li'):
    Producer = laptop.span.text
    specs = laptop.find('a', {'class': 'product-list__name'}).text
    price = laptop.find('span', {'class': 'price__number'}).text.split()
    price = ' '.join(map(str, price))
    currency = laptop.find('span', {'class': 'price__currency'}).text
    cost = price + " " + currency
    print(Producer)
    print(specs)
    print(cost)
    print()

    csv_writer.writerow([Producer, specs, cost])

csv_file.close()
