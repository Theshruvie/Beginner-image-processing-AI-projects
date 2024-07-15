import cv2
import numpy as np

img=cv2.imread('C://Users//dell//Documents//AI PROJECTS//BEGINNERS//41429.jpg')

#Gaussian blur
gs=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("gaussian blurring",gs)
cv2.imshow("orginal",img)

#Median blur
mb=cv2.medianBlur(img,5)
cv2.imshow("median blur",mb)

#Bilateral blurring
bilblur=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bil blurig",bilblur)
