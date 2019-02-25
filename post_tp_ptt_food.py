import requests
from  bs4 import BeautifulSoup
res = requests.get('https://www.ptt.cc/bbs/Food/index.html', verify=False)
soup = BeautifulSoup(res.text)
#print(soup)

for entry in soup.select('.r-ent'):
    print("title: %s" % entry.select('.title')[0].text.replace("\n", ""))
    print("author: " +entry.select('.author')[0].text)
    print("date: " +entry.select('.date')[0].text)
    





