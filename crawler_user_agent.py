import requests
from bs4 import BeautifulSoup
import json
url = 'https://buy.yungching.com.tw/ws/GetCustomerPromoteCase'
payload = {
'condition':'%E5%8F%B0%E5%8C%97%E5%B8%82-_c/',
'page': 'buylist',
'random':4,
'Wmxuid': False
}
res = requests.post(url, data = payload)
#print(res.text)
soup = BeautifulSoup(res.text)
#print(soup)
list = soup.select('p')[0].text
#print(list)
json_data = json.loads(list)
#print(json_data)
#print(json_data['ObjInfo'])
ObjInfo = json_data['ObjInfo']
#print(ObjInfo)


for item in ObjInfo:
    print("建案: " + item['CaseName'] + " 地址: "+item['Address'] + " 地區:" + item['District'])
    print("說明: " + item['CaseFeature'] + " 類型: "+item['CaseTypeName'] + " 總價: "+str(item['Price']))
    print("地坪: " + str(item['Landpin']) + " 建坪: " + str(item['RegArea']))


#print(timetable_json);#找最後的值






