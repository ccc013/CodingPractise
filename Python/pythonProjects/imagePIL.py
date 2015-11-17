# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:29:29 2015

@author: cai
"""
from __future__ import print_function
from PIL import Image
import time, os

rootPath = '/home/cai/dataset/foodIngredients/images/'
newPath = rootPath + 'resize_512/'
txtFile = rootPath + 'rotate.txt'
startTime = time.ctime()
print("start rotating images: %s" % startTime)
count = 0
with open(txtFile,'r') as fr:
    imageDirList = fr.readlines()
    for idx, name in enumerate(imageDirList):
        imageDir = newPath + name.strip() + '/'
        imageList = [x for x in os.listdir(imageDir)]
        imageList = sorted(imageList)
        for idx, img in enumerate(imageList):
            imageName = imageDir + img
            img = Image.open(imageName)
            outImg = img.transpose(Image.ROTATE_90)            
            newImageName = imageName.replace('_resMax', '_resMax_rotate')
            if os.path.isfile(newImageName):
                continue
            outImg.save(newImageName)
            count += 1
            if idx == 10:
                break
            print("finisn %d images" % count)

endTime = time.ctime()
print("End at %s" % endTime)
print("finsh %d images" % count)
        

#==============================================================================
# img = Image.open("corn.jpg")
# out = img.transpose(Image.ROTATE_180)
# out.save("rotate_180.jpg")
#==============================================================================



#img.thumbnail((new_w, new_y), Image.ANTIALIAS)
#img.thumbnail((700, 600), Image.ANTIALIAS)
#img.save("thumb_img.jpg")
#img.save("thumb_img_big.jpg")
#res_img = img.resize((new_w, new_y), Image.ANTIALIAS)
#big_img = img.resize((700, 600), Image.ANTIALIAS)
#res_img.save("res_img_PIL.jpg")
#res_img.save("res_img_PIL_95.jpg", quality = 95)
#big_img.save("big_img_PIL.jpg", quality = 95)
