from bs4 import BeautifulSoup
import requests
from webull import webull

url = 'https://coinmarketcap.com/currencies/shiba-inu/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
div_price = soup.find('div', class_="price")
price = div_price.div.text

print(price)
