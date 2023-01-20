import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/s?k='
product = 'iphone'

response = requests.get(url + product)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='s-result-item')
for product in products:
    title = product.find('span', class_='a-size-medium a-color-base a-text-normal').text
    price = product.find('span', class_='a-price-whole').text
    print(title, price)
