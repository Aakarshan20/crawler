import requests
import cv2
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
url = 'http://bsr.twse.com.tw/bshtm/bsMenu.aspx'

res = requests.get(url)
soup = BeautifulSoup(res.text)
target_img = soup.select('#Panel_bshtm')[0].select('img')[0]['src'];



#print(res.text)

print(target_img)

target_url = 'http://bsr.twse.com.tw/bshtm/' + target_img

print(target_url)

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, -1)
    return image
image = cv2.imread("capture.jpg")
#plt.imshow(image)
#print(type(image))
#print(image.shape)


#cv2.imshow('my img', image)

#image = url_to_image(target_url)

cv2.imshow('(1)I am image', image)


kernel = np.ones((4,4), np.uint8)
erosion = cv2.erode(image, kernel, iterations=1)
#cv2.imshow('(2)I am erosion', erosion)

blurred = cv2.GaussianBlur(erosion, (5,5),0)
#cv2.imshow('(3)I am blurred', blurred)

edged = cv2.Canny(blurred, 30, 150)#邊緣偵測
#cv2.imshow('(4)I am edged', edged)

dilation = cv2.dilate(edged, kernel, iterations = 1)#膨脹
cv2.imshow('(5)I am dilation', dilation)

#偵測輪廓

#print(cv2.RETR_TREE)
#print(cv2.CHAIN_APPROX_SIMPLE)

#下面那行是錯的
#image, contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(contours)

cnts = sorted([(c, cv2.boundingRect(c)[0]) for c in contours], key = lambda x: x[1])



#找出字型邊界的x y軸 長寬等等
ary = []
for (c,_) in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    #print(x,y,w,h)
    if w>15 and h>15:#只有寬高大於15的才放入array
        ary.append((x,y,w,h))


print(ary)

fig = plt.figure()
for id, (x,y,w,h) in enumerate(ary):
    roi = dilation[y:y+h, x:x+w]#找出膨脹後的結果把值丟回去
    #print(roi)
    thresh = roi.copy()
    
    a = fig.add_subplot(1, len(ary), id+1)
    #print(1)
    plt.imshow(thresh)
    #cv2.imshow('aaa', thresh)
    


print("OK")







































