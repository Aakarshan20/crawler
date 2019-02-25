import requests
import cv2
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
import numpy as np

from sklearn.preprocessing import binarize


img = cv2.imread("capture.jpg")



#如果去噪不明顯 修改第三 第四個參數 (調大)
dst = cv2.fastNlMeansDenoisingColored(img, None, 30, 30, 7, 21)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dst)



#將圖片變成黑白(去除灰)
#plt.subplot(121)
ret, thresh = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY_INV)#反轉黑白
ret, thresh = cv2.threshold(thresh, 127, 255, cv2.THRESH_BINARY_INV)#再轉一次
#plt.subplot(121)
plt.imshow(thresh)
#plt.subplot(122)
#plt.imshow(thresh2)
#plt.imshow(thresh)


imgarr = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)#專為numpy矩陣


plt.show()#印出圖片

kernel = np.ones((4,4),np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('(2)I am erosion',erosion)

blurred = cv2.GaussianBlur(erosion, (5,5),0)
cv2.imshow('(3)I am blurred', blurred)

edged = cv2.Canny(blurred, 30, 150)#邊緣偵測
cv2.imshow('(4)I am edged', edged)

dilation = cv2.dilate(edged, kernel, iterations = 1)#膨脹
cv2.imshow('(5)I am dilation', dilation)

#ret, thresh = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY_INV)#反轉黑白
#ret, thresh = cv2.threshold(thresh, 127, 255, cv2.THRESH_BINARY_INV)#再轉一次


#print(imgarr)#可見大部份的值都是黑色的
#print(imgarr.shape)


#print(imgarr.shape)
#print(imgarr)













































