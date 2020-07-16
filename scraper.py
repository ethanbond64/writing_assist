import requests
from bs4 import BeautifulSoup
import re
# URL = 'https://medium.com/@[author]'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    print(link.get('href'))
