# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:35:23 2015

@author: cai
"""
from __future__ import print_function
from PIL import Image
import os
import numpy as np
import cv2
import cv2.cv as cv
import random

# flip the image, and return the flipped image
# mode: 0 is left_right, 1 is top_down
def flipImage(imagePath, mode = 0):
    try:
        img = Image.open(imagePath)
        if 0 == mode:
            return img.transpose(Image.FLIP_LEFT_RIGHT)
        elif 1 == mode:
            return img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            print('invalid mode, mode should be 0 or 1!')
    except IOError as e:
        print('Error opening the image,',e)
    return img

# rotate the image use PIL
def rotateImagebyPIL(imagePath, angle = 45):
    try:
        img = Image.open(imagePath)
        return img.rotate(angle)
    except IOError as e:
        print('Error opening the image,',e)

# rotate the image use OpenCV
def rotateImagebyCV(imagePath, angle = 45):
    try:
        img = cv2.imread(imagePath)
        img_center = tuple(np.array(img.shape) / 2)
        rot_mat = cv2.getRotationMatrix2D((img_center[0],img_center[1]), angle, 1.0)
        return cv2.warpAffine(img, rot_mat, img.shape[:2], flags = cv2.INTER_LINEAR)
    except IOError as e:
        print('Error opening the image,',e)

# crop
def cropImage(imagePath):
    try:
        img = Image.open(imagePath)
        width, height = img.size
        newWidth, newHeight = (width - 20), (height - 20)
        box = (0, 0, newWidth, newHeight)
        return img.crop(box)
    except IOError as e:
        print('Error opening the image,',e)
        
# 生成训练集和测试集，可以修改函数中训练集和测试集的文件夹路径
#   filePath：原始数据集的文件路径
def generateTrainOrTestCollection(filePath):
    filelists = [x for x in os.listdir(filePath)]
    #filelists = sorted(filelists)
    random.shuffle(filelists)
    lens = len(filelists)
    trainNums = int(0.8 * lens)
    print('trainNums: ',trainNums)
    for idx, _file in enumerate(filelists):
        path = os.path.join(filePath, _file.strip())
        
        if os.path.isfile(path):
             # split the image to train and test set 
             try:
                 img = Image.open(path)
             except IOError as e:
                 print('can not open :', path)
                 print('error: ',e)
             #print('processing',path)
             imagelist = path.split('/')
             trainImagePath = os.path.join(root_Path,'part1/trainImages',imagelist[-2],_file.strip())
             testImagePath = os.path.join(root_Path,'part1/testImages',imagelist[-2],_file.strip())
             # 如果文件已经存在则跳过
             if os.path.isfile(trainImagePath) or os.path.isfile(testImagePath):
                 continue
             if idx < trainNums:
                 img.save(trainImagePath)
                 #print('finished',trainImagePath)
             else:
                 img.save(testImagePath)
                 #print('finished',testImagePath)
        elif os.path.isdir(path):
            generateTrainOrTestCollection(path)

# 数据拓展,可以修改函数中用来拓展数据的方法，默认是使用flipImage()这个方法进行水平或垂直翻转图片
# classTxtFile: 保存类名字的文件       imagePath:图像的总路径
def data_argumentation(classTxtFile,imagePath):
    i = 0
    fr = open(classTxtFile,'r')
    nameList = fr.readlines()
    for idx,dirName in enumerate(nameList):
        imageDirPath = os.path.join(imagePath,nameList[idx].strip())
        imageList = [x for x in os.listdir(imageDirPath)]
        imageList = sorted(imageList)
        
        
        for n in imageList:
            image = os.path.join(imageDirPath,n)
            
            #convertToGreyImage2(image,image)
            resizeImageByPIL(image,128,128,image)
            i += 1
#==============================================================================
#             newName = image.replace('.jpg','_flip.jpg')
#             print(newName)
#             img = flipImage(image)
#             img.save(newName)
#==============================================================================
    fr.close()
    print(i)
# 生成训练和测试集的标签文件,可以根据需要修改标签文件的内容
# classTxtFile: 保存类名字的文件； 
# trainDirPath: 训练集文件路径；  testDirPath: 测试集文件路径
def generateTrainOrTestLabelFile(classTxtFile,trainDirPath,testDirPath):
    fr = open(classTxtFile, 'r')
    ftrain = open(trainTxtFile, 'w')
    ftest = open(valTxtFile, 'w')
  
    nameLists = fr.readlines()
    nameLists = sorted(nameLists)
    for label,name in enumerate(nameLists):
        print('processing',unicode(name))
        # 训练集和测试集的文件路径
        imageTrainDirPath = os.path.join(trainDirPath, name.strip())
        imageTestDirPath = os.path.join(testDirPath, name.strip())
        names_train = [x for x in os.listdir(imageTrainDirPath)]
        names_test = [x for x in os.listdir(imageTestDirPath)]
        # 将训练集的图片路径写入训练集标签文件
        for name in names_train:
            fullname = os.path.join(imageTrainDirPath, name)
            # 标签文件的内容
            info = fullname.replace(trainDirPath, 'images/trainImages-128/') + ' ' + str(label) + '\n'
            ftrain.write(info)
        
        # 生成测试集的标签文件
        for name in names_test:
            fullname = os.path.join(imageTestDirPath, name)
            info = fullname.replace(testDirPath, 'images/testImages-128/') + ' ' + str(label) + '\n'
            ftest.write(info)
            
    fr.close()
    ftrain.close()
    ftest.close()
    print('finish!')

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

# 图像灰度化处理
def convertToGreyImage(imagePath,newImagePath):
    image = cv.LoadImage(imagePath)
    new = cv.CreateImage(cv.GetSize(image), image.depth, 1)
    for i in range(image.height):
        for j in range(image.width):
            new[i,j] = 0.3 * image[i,j][0] + 0.59 * image[i,j][1] +  0.11 * image[i,j][2]
    cv.SaveImage(newImagePath,new)
    
# 图像灰度化处理2
def convertToGreyImage2(imagePath,newImagePath):
    img = Image.open(imagePath).convert('L')
    img.save(newImagePath)
    
# resize
def resizeImageByPIL(imagePath,newWidth,newHeight,newImagePath):
    img = Image.open(imagePath)
    img = img.resize((newWidth,newHeight),Image.BICUBIC)
    img.save(newImagePath)

if __name__ == '__main__':
    root_Path = '/home/cai/dataset/foodIngredients-68'
    imagePath = os.path.join(root_Path , 'images/')
    txtFilePath = os.path.join(root_Path, 'data/')
    
    classTxtFile = os.path.join(root_Path,'data/', 'classes.txt')
    trainDirPath = os.path.join(imagePath,'trainImages-128/')
    testDirPath = os.path.join(imagePath,'testImages-128/')
    
    trainTxtFile = os.path.join(txtFilePath,'train_meta_128.txt')
    valTxtFile = os.path.join(txtFilePath,'val_meta_128.txt')
    
    # 图像灰度化处理
    #convertToGreyImage(img,new)
    
    # 数据拓展
    #data_argumentation(classTxtFile,trainDirPath)
    #data_argumentation(classTxtFile,testDirPath)
    
    # 生成训练集和测试集
    #generateTrainOrTestCollection(imagePath)
    
    # 生成训练和测试集的标签文件
    
    #generateTrainOrTestLabelFile(classTxtFile, trainDirPath, testDirPath)
    
    
    # 测试写入的图片路径是否正确
    #test_image(trainTxtFile,valTxtFile,root_Path)  
    

        
