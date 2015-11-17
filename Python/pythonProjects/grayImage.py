# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:54:01 2015

@author: cai
"""

'transfer rgb to gray image and save,then save the filename to a new txt file'

import cv2
import os

root_path = '/home/cai/dataset/food-101/'
txtPath = root_path + 'data/'

trainTxt = txtPath + 'train_meta.txt'
valTxt = txtPath + 'val_meta.txt'

newTrainTxt = txtPath + 'train_gray_meta.txt'
newValTxt = txtPath + 'val_gray_meta.txt'

def rgbToGray(oldTxtPath,newTxtPath,path):
    contentList = []
    with open(oldTxtPath) as fr:
        fw = open(newTxtPath,'w+')
        contentList = fr.readlines()
        lens = len(contentList)
        #print 'length = ', lens
        for i in range(lens):
            content = contentList[i].split(' ')
            imageName = content[0].strip()
            imagePath = root_path + imageName
            grayImage = cv2.imread(imagePath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            #print grayImage.shape
            saveImagePath = root_path + path + imageName
            #print saveImagePath
            cv2.imwrite(saveImagePath, grayImage)
            newContent = path + imageName + " " + content[1]
            fw.write(newContent)
            #print newContent
            print 'finish ', i
        fw.close()
        
# test
trainPath = "trainImages/gray_"
valPath = "testImages/gray_"
print "trainImages start..."
rgbToGray(trainTxt, newTrainTxt, trainPath)
print "testImages start..."
rgbToGray(valTxt, newValTxt, valPath)
print "Done!"