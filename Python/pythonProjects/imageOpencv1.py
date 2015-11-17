# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:22:33 2015

@author: cai
"""
from __future__ import print_function
import cv2 
import cv2.cv as cv
import time

# read image
img = cv2.imread("pizza1.jpg")
img2 = cv2.imread("corn.jpg")
start = time.time()
localTime = time.ctime()
print(localTime)
res_img = cv2.resize(img2,(256,256),interpolation = cv2.INTER_AREA)
print(img.shape)
#smallToBig_img = cv2.resize(img2,(700,600),interpolation = cv2.INTER_AREA)
#cv2.imwrite("smallToLarge_area.jpg", smallToBig_img)
#cv2.imwrite("resize_img_small_area.jpg", res_img)
end = time.time()
#print(end - start)
print(time.ctime())
print(time.localtime())
print(time.gmtime())
#==============================================================================
# image = cv.LoadImage("pizza1.jpg")
# b = cv.CreateImage(cv.GetSize(image), image.depth, 1)
# g = cv.CloneImage(b)
# r = cv.CloneImage(b)
# 
# cv.Split(image, b, g, r, None)
# cv.ShowImage("image", r)
# 
#==============================================================================
cv.WaitKey(0)
#==============================================================================
# img = cv2.imread('pizza1.jpg',1)
# grayImg = cv2.imread('pizza1.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
# 
# print 'original image shape: ', img.shape
# print 'gray image shape: ', grayImg.shape
# 
# print 'original image size: ', img.size
# print 'gray image size: ', grayImg.size
# 
# print 'original image type: ', img.dtype
# print 'gray image type: ', grayImg.dtype
# cv2.imwrite('gray_pizza1.png', grayImg)
#==============================================================================
# resize the image
#==============================================================================
# im = cv.LoadImage('pizza1.jpg')
# thumb = cv.CreateImage((im.width / 2, im.height / 2), 8, 3)
# cv.Resize(im,thumb)    # resize the original image into thumb
# cv.SaveImage('pizza1_thumb1.png',thumb)
# 
# height, width = img.shape[:2]
# thumb2 = cv2.resize(img,(2 * width, 2 * height), interpolation = cv2.INTER_CUBIC)
# cv2.imwrite('pizza1_thumb2.png',thumb2)
#==============================================================================



#==============================================================================
# # show the image
# cv2.imshow('image',img);
# 
# k = cv2.waitKey(0);
# if k == 27:     # wait for ESC key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):   # wait for 's' key to save and exit
#     cv2.imwrite('messigray.png', img)
#     cv2.destroyAllWindows()
#==============================================================================
    

