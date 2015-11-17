# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:58:25 2015

@author: cai

A function use to write filename and its label to a txt file
"""

import os

dirPath = '/home/cai/dataset/food-101/'
imagePath = dirPath + 'images/'
txtFilePath = dirPath + 'data/'

# set train and val txt file name
trainTxtName = 'train.txt'
valTxtName = 'val.txt'

# read dirName
def read(path = '.'):
    # 
    dirList = [x for x in os.listdir(path)]
    # sort dirList by a to z
    dirList = sorted(dirList)
    for label, name in enumerate(dirList):
        dirname = imagePath + name + '/'
        #print str(label) + ' ' + name
        # put all the image filename to a list
        imagesList = [x for x in os.listdir(dirname)]
        # use 750 images to train 
        trainList = imagesList[:750]
        # use 250 images to val
        valList = imagesList[750:]
        trainFilename = txtFilePath + trainTxtName
        valFilename = txtFilePath + valTxtName       
        writeToTxt(name,label,trainFilename,trainList)
        writeToTxt(name,label,valFilename,valList)
        
# write filename and label to file
def writeToTxt(path,label,filename,data):
    with open(filename,'a') as fw:
        for i in data:
           # info = path + i + ' ' + str(label) + '\n'
             
           info = path + '/' + i + ' ' + str(label) + '\n'            
           fw.write(info)
  
# Test
read(imagePath)
  