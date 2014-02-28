#coding=utf-8
import cv2,cv
import numpy as np
import coconut as co
import math


img = cv2.imread('/Users/zyw/t2.png',0)
#OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(7, 7))

#腐蚀图像
eroded = cv2.erode(img,kernel)
#显示腐蚀后的图像
cv2.imshow("Eroded Image",eroded);

#膨胀图像
dilated = cv2.dilate(eroded,kernel)
#显示膨胀后的图像
cv2.imshow("Dilated Image",dilated);
#原图像
cv2.imshow("Origin", img)
'''
#NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3,3)))
Nperoded = cv2.erode(img,NpKernel)
#显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel",Nperoded);
'''
cv2.waitKey(0)
cv2.destroyAllWindows()

