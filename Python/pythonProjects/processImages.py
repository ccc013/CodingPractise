# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:47:20 2015

@author: cai

将所有图片分成训练集和测试集，并分别写入两个txt文件中
"""
from __future__ import print_function
import os
import time
import cv2

rootPath = '/home/cai/dataset/foodIngredients/images/'
imageDirPath = rootPath + 'resize_512/'
classFilePath = rootPath + 'classes.txt'

# 保存训练和测试图片标签的TXT文件
trainTxt = rootPath + 'train_meta.txt'
valTxt = rootPath + 'val_meta.txt'

startTime = time.ctime()
print("start at %s" % startTime)
ft = open(trainTxt,'w')
fv = open(valTxt, 'w')

imageDirList = [x for x in os.listdir(imageDirPath)]
imageDirList = sorted(imageDirList)
count = 0
for idx, name in enumerate(imageDirList):
    imageFilePath = imageDirPath + name + '/'
    #print(imageFilePath)
    imageFileList = [x for x in os.listdir(imageFilePath)]
    lens =len(imageFileList)
    # 获得训练图片数量和测试图片数量
    trainNums = int(0.7 * lens)
    testNums = lens - trainNums
    #print(trainNums)
    for i, img in enumerate(imageFileList):
        imagePath = imageFilePath + img
        #print(imagePath + '\n' + str(i))
        try:
            img = cv2.imread(imagePath)
        except:
            print("cannot open the %s" % imagePath)
        
        if i < trainNums:
            newTrainImagePath = imagePath.replace('/home/cai/dataset/foodIngredients/images/resize_512', 
                                                  'images/trainImages').strip()
            cv2.imwrite(newTrainImagePath, img)
            ft.write(newTrainImagePath + '\t' + str(idx) + '\n')
        else:
            newTestImagePath = imagePath.replace('/home/cai/dataset/foodIngredients/images/resize_512',
                                                 'images/testImages').strip()
            cv2.imwrite(newTestImagePath, img)
            fv.write(newTestImagePath + ' ' + str(idx) + '\n')
        count += 1
        print("finish %d image" % count)
    #if idx == 2:
        #break
    
endTime = time.ctime()
print("end at %s" % endTime)
print("finish %d images" % count)
ft.close()
fv.close()