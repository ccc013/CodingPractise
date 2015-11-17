# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 15:35:23 2015

@author: cai
"""
from __future__ import print_function
from PIL import Image
import os, sys
import numpy as np
from random import randint
import time
import cv2

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
        
# 递归读取文件，
def read_file(filePath='.'):
    filelists = [x for x in os.listdir(filePath)]
    #filelists = sorted(filelists)
    lens = len(filelists)
    trainNums = int(0.7 * lens)
    for idx, _file in enumerate(filelists):
        path = os.path.join(filePath, _file)
        print('processing',path)
        if os.path.isfile(path):
             # split the image to train and test set  
             img = Image.open(path)
             trainImagePath = path.replace('resize_512','trainImages').strip()
             testImagePath = path.replace('resize_512','testImages').strip()
             if os.path.isfile(trainImagePath) or os.path.isfile(testImagePath):
                 continue
             if idx < trainNums:
                 img.save(trainImagePath)
             else:
                 img.save(testImagePath)
             
#             newImage = rotateImagebyPIL(path, 90)
#             newImagePath = os.path.splitext(path)[0] + '_rotate.jpg'
#             newImage.save(newImagePath)
#==============================================================================
            
        elif os.path.isdir(path):
            read_file(path)

if __name__ == '__main__':
    root_Path = '/home/cai/dataset/foodIngredients/images/'
    classTxtPath = os.path.join(root_Path, 'camera_classes.txt')
    trainTxtPath = os.path.join(root_Path,  'total_train.txt')
    testTxtPath = os.path.join(root_Path, 'total_test.txt')
   
    fr = open(classTxtPath, 'r')
    ftrain = open(trainTxtPath, 'w')
    ftest = open(testTxtPath, 'w')
    
    # 生成训练和测试集的标签文件
    nameLists = fr.readlines()
    for label,name in enumerate(nameLists):
        print('processing',unicode(name))
        imageTrainDirPath = os.path.join(root_Path, *('total_trainImages/' ,name.strip()))
        imageTestDirPath = os.path.join(root_Path, *('total_testImages/', name.strip()))
        names = [x for x in os.listdir(imageTrainDirPath)]
        names_test = [x for x in os.listdir(imageTestDirPath)]
        for name in names:
            fullname = os.path.join(imageTrainDirPath, name)
            info = fullname.replace(root_Path, 'images/') + ' ' + str(label) + '\n'
            ftrain.write(info)
        for name in names_test:
            fullname = os.path.join(imageTestDirPath, name)
            info = fullname.replace(root_Path, 'images/') + ' ' + str(label) + '\n'
            ftest.write(info)
        #read_file(imageDirPath)
    fr.close()
    ftrain.close()
    ftest.close()
    
    ftrain = open(trainTxtPath, 'r')
    ftest = open(testTxtPath, 'r')
    
    trainFiles = ftrain.readlines()
    testFiles = ftest.readlines()
    # 测试写入的图片路径是否正确
    for name in trainFiles:
        n = '/home/cai/dataset/foodIngredients/' + name.split(' ')[0].strip()
        try:        
            img = Image.open(n)
        except IOError as e:
            print("Error open the image:",n)
    print('train images ok!')
    
    for name in testFiles:
        n = '/home/cai/dataset/foodIngredients/' + name.split(' ')[0].strip()
        try:        
            img = Image.open(n)
        except IOError as e:
            print("Error open the image:",n)
    print('test images ok!')    
    
    
#==============================================================================
#     imagePath = os.path.join(root_Path, 'IMG_17.jpg')
#     r_image = rotateImagebyPIL(imagePath, 270)
#     newImagePath = os.path.splitext(imagePath)[0] + '_rotate270' + '.jpg'
#     r_image.save(newImagePath)   
#==============================================================================
    

        