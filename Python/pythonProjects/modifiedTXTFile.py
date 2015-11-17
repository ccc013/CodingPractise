# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:59:53 2015

@author: cai
"""

import os

txtFilePath = '/home/cai/dataset/food-101/data/'

trainFilename = txtFilePath + 'train.txt'
valFilename = txtFilePath + 'val.txt'

newTrainFile = txtFilePath + 'train_new1.txt'
newValFile = txtFilePath + 'val_new1.txt'

contentList = []

def modifiedTxt(oldFilePath,newFilePath,lineNums,labelNum):
    with open(oldFilePath) as fr:
        fw = open(newFilePath,'a')
        for i in range(0,lineNums):    
            content = fr.readline()
            label = i / labelNum
            
            fw.write((r'images/'+content)) # + '.jpg ' + str(label) + '\n'))
            #contentList.append((content + '.jpg ' + str(label) ))
        fw.close()
#with open(newTrainFile,'w') as fw:
    #fw.write(contentList[:10])

# 
if __name__ == '__main__':
    modifiedTxt(trainFilename, newTrainFile, 75750, 750)
    modifiedTxt(valFilename, newValFile, 25250, 250)