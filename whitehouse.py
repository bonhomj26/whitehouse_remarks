# Obtain the links from:
# https://www.whitehouse.gov/briefings-statements/

# Goal: Extract all of the links on the page that point to the briefings and statements

import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls =[]
for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find('a')\
    urls.append(a_tag.attrs['href']) # This not only returns the a tag but also the href attribute.
    
print(urls)