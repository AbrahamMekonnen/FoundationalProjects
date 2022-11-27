import bs4,re,lxml
import requests
from bs4 import BeautifulSoup

result = requests.get("http://hrlibrary.umn.edu/peace/senate.html")
src = result.content[:100000]
soup = BeautifulSoup(src, 'lxml')
pattern = re.findall(r'[\w\d._*()^%$#@!]+@[\w\d]+\.[\w]+',soup.get_text())
print(pattern[:20])

