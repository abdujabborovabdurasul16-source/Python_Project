import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/IBM'
headers = {'User-Agent': 'Mozilla'}
response = requests.get(url, headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
print(html_content[:500])