# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:11:32 2016

@author: cai

处理CUB-200-2011数据库的数据，生成标签文件，lmdb等
"""
from __future__ import print_function
from __future__ import division
import os
import shutil
from PIL import Image

# create folder from the filename in a txtFile
def createFolder(filename, *dirPath):
    nameLists = []
    with open(filename,'r') as fr:
        nameLists = fr.readlines()
        lens = len(nameLists)
        for direct in dirPath:
            print('processing', direct)
            for idx in range(lens):
                fileName = nameLists[idx].split(' ')[1].strip()
                folder = os.path.join(direct, fileName) 
                if not os.path.isdir(folder):
                    os.mkdir(folder)
                print('make ', (idx+1))

# copy src to dst
def copyFile(src,dst):
    shutil.copyfile(src,dst)
    
# generate train/test collection
def generateTrainOrTestCollection(imagesTxt,splitTxt):
    fi = open(imagesTxt, 'r')
    fs = open(splitTxt, 'r')
    ft = open(trainTxt, 'w')
    fv = open(testTxt, 'w')
    
    imagesList = fi.readlines()
    splitList = fs.readlines()
    trainNums = 0
    testNums = 0
    
    for img, spl in zip(imagesList, splitList):
        imgName = img.split(' ')[1]
        isTrain = spl.split(' ')[1]
        
        #print("image--{0}, isTrain--{1}".format(imgName,isTrain))
        if int(isTrain) == 1:
            originPath = os.path.join(imagePath, imgName.strip())
            trainPath = os.path.join(trainImagePath, imgName.strip())
            
            label_str = imgName.split('.')[0]
            label = int(label_str)
            print("originPath--{0}\ntrainPath--{1},label={2}\n".format(originPath,trainPath,label))
            #copyFile(originPath,trainPath)
            content = trainPath.replace(trainImagePath,'trainImages') + ' ' + str(label) + '\n'
            ft.writelines(content)
            trainNums += 1
        elif int(isTrain) == 0:
            originPath = os.path.join(imagePath, imgName.strip())
            testPath = os.path.join(testImagesPath, imgName.strip())
            label_str = imgName.split('.')[0]
            label = int(label_str)
            print("originPath--{0}\ntestPath--{1},label={2}\n".format(originPath,testPath,label))
            #copyFile(originPath,testPath)
            content = testPath.replace(testImagesPath,'testImages') + ' ' + str(label) + '\n'
            fv.writelines(content)
            testNums += 1
        
        
    fi.close()
    fs.close()
    ft.close()
    fv.close()
    print("trainImagesNums = {0}, testImagesNums = {1}".format(trainNums,testNums))

# 测试写入的图片路径是否正确
# trainTxtFile: 训练集文件路径    valTxtFile:测试集文件路径
# root_Path:根目录
def test_image(trainTxtFile, valTxtFile,root_Path):
    ftrain = open(trainTxtFile, 'r')
    ftest = open(valTxtFile, 'r')
    
    trainFiles = ftrain.readlines()
    testFiles = ftest.readlines()
   
    for name in trainFiles:
        n = os.path.join(root_Path ,name.split(' ')[0].strip())
        try:        
            img = Image.open(n)
        except IOError as e:
            print("Error open the image:",n)
    print('train images ok!')
    
    for name in testFiles:
        n = os.path.join(root_Path,name.split(' ')[0].strip())
        try:        
            image = Image.open(n)
        except IOError as e:
           print("Error open the image:",n)
    print('test images ok!')

if __name__ == '__main__':
    rootPath = '/home/cai/dataset/CUB_200_2011'
    imagePath = os.path.join(rootPath, 'images')
    trainImagePath = os.path.join(rootPath,'trainImages')
    testImagesPath = os.path.join(rootPath,'testImages')
    classesTxt = os.path.join(rootPath,'classes.txt')
    imagesTxt = os.path.join(rootPath,'images.txt')
    splitTxt = os.path.join(rootPath,'train_test_split.txt')
        
    
    trainTxt = os.path.join(rootPath,'data','train_meta.txt')
    testTxt = os.path.join(rootPath,'data','test_meta.txt')
    
    # generate train/test collection
    #generateTrainOrTestCollection(imagesTxt, splitTxt)
    
    # test
    #test_image(trainTxt, testTxt, rootPath)
    
