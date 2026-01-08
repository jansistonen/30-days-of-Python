# WEB SCRAPING LETS GOOOO

# requests already installed
# installed pip beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
#check status
status = response.status_code

print(status)