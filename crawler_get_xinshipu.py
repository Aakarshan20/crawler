import requests
from bs4 import BeautifulSoup

url = 'https://www.xinshipu.com/zuofa/666593'
res = requests.get(url)
soup = BeautifulSoup(res.text)#, features="lxml")
reup = soup.select('.w tc header')
title = soup.select('h1')[1].text
number = soup.select(".cg2 mt12")
#print(soup);
print(reup);
print(title)
print(number)
#print(views)
#print(notes)
#print(score)
'''
soup = BeautifulSoup(res.text)
reviews = soup.select('script')[-1].text
print(timetable_json);#找最後的值
'''
