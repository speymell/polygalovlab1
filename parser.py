import requests
from bs4 import BeautifulSoup

response = requests.get('https://2ip.ru/')
soup = BeautifulSoup(response.content, 'html.parser')

my_ip = soup.find('div', class_='ip')
print(my_ip.text)