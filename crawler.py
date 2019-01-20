import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.gamer.com.tw/")
soup = BeautifulSoup(res.text)



for item in soup.select('#gamechart-growth'):
    gamename = item.select('.game')
    gamedata = item.select('.game-data')
    urls = item.select('.go-forum')
    #print("%s: %s" % (gamename, gamedata))
    #print(item)
    #print(gamename)
    #alldata.append((gamename, gamedata))
    
gamenames = []

for name in gamename:
    gamenames.append(name.text.strip())

#for datumA, datumB in alldata:
    #print(datumA, datumB)

allgamedata = []

for data in gamedata:
    allgamedata.append(data.text.strip())

urllist = []

for url in urls:
    urllist.append(url['href'])

#for a in soup.find_all('a', href=True):
    #print "Found the URL:", a['href']

counter =0
for i in gamenames:
    print(i + ":" + allgamedata[counter] + ", 哈拉區: " + urllist[counter])
    counter +=1





