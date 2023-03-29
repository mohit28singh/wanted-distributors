import bs4
import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.bseindia.com')
soup=bs4.BeautifulSoup(r.text,'xml')
print(soup)

