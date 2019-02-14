import requests
import os
from bs4 import BeautifulSoup
import sqlite3 as lite
import shutil

#print(os.getcwd())

#BASE_DIR = os.path.dirname(os.path.abspath('ex1.db'))

#print(BASE_DIR)

response = requests.get('https://cdn2.ettoday.net/images/3896/d3896303.jpg', stream=True)

print(response)

f = open('image.jpg', 'wb')
shutil.copyfileobj(response.raw,f)
f.close()


con = lite.connect('C:/Users/user/ex1')



cur = con.cursor()

f = open('image.jpg', 'rb')
ablob = f.read()
f.close()

cur.execute('insert into image_tb(img) values (?)', [lite.Binary(ablob)])

con.commit()
con.close()





