#火車時刻表post查詢
#http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx
'''
FromCity	0
FromStation	1008
FromStationName	0
ToCity	5
ToStation	1206
ToStationName	0
TrainClass	2
searchdate	2019-01-21
FromTimeSelect	0000
ToTimeSelect	2359
Timetype	1
'''
import requests
from bs4 import BeautifulSoup

url = 'http://twtraffic.tra.gov.tw/twrail/TW_SearchResult.aspx'
payload = {
'FromCity':'0',
'FromStation':'1008',
'FromStationName':'0',
'ToCity':'5',
'ToStation':'1206',
'ToStationName':'0',
'TrainClass':'2',
'searchdate':'2019-01-21',
'FromTimeSelect':'0000',
'ToTimeSelect':'2359',
'Timetype':'1'
}
res = requests.post(url, data = payload)
#print(res.text)
soup = BeautifulSoup(res.text)
timetable_json = soup.select('script')[-1].text
print(timetable_json);#找最後的值






