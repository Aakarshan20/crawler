import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}

url = 'https://statementdog.com/analysis/tpe/1101'
res = requests.get(url, headers = headers)

print(res.text)

