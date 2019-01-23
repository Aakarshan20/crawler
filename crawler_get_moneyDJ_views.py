import requests
#from bs4 import BeautifulSoup


url = 'https://www.moneydj.com/InfoSvc/apis/vc'
payload = '{"counts":[{"svc":"NV","guid":"1293d9fc-f4eb-4602-b798-8d388a216ceb"}]}'
head = {'Content-Type':'application/json'}

res = requests.post(url, data = payload, headers = head)
print(res.text)
'''
soup = BeautifulSoup(res.text)
reviews = soup.select('script')[-1].text
print(timetable_json);#找最後的值
'''
