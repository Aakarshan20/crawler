import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}

url = 'https://www.tdcc.com.tw/smWeb/QryStock.jsp'
payload = {
'REQ_OPR':'qrySelScaDates'
}
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/65.0'}



res = requests.post(url, headers = headers, data = payload)



print(res.text)
