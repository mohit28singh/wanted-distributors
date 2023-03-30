import requests
from bs4 import BeautifulSoup

url = 'https://www.bseindia.com'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('div', class_='gainlosetabbox')
    if data is not None:
        print(data)
    else:
        print('Could not find data.')
else:
    print(f'Request failed with status code {response.status_code}.')
