# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:32:34 2015

@author: cai
"""
from __future__ import print_function
from __future__ import division
import os,sys
import shutil
import cv2

# create folder from the filename in a txtFile
def createFolder(filename, *dirPath):
    nameLists = []
    with open(filename,'r') as fr:
        nameLists = fr.readlines()
        lens = len(nameLists)
        for direct in dirPath:
            print('processing', direct)
            for idx in range(lens):
                folder = os.path.join(direct, nameLists[idx].strip()) 
                if not os.path.isdir(folder):
                    os.mkdir(folder)
                print('make ', (idx+1))

# 递归读取文件，并对文件进行重命名, 调整图片大小
def read_file(filePath='.'):
    filelists = [x for x in os.listdir(filePath)]
    filelists = sorted(filelists)
    for idx, _file in enumerate(filelists):
        path = os.path.join(filePath, _file)
        print('processing',path)
        if os.path.isfile(path):
            newName = _file[:4] + str(idx) + _file[-4:]
            newName = os.path.join(filePath, newName)
            os.rename(path, newName)
            #resizeImage(path, 1040)
        elif os.path.isdir(path):
            read_file(path)

# resize image
def resizeImage(imagePath, maxValue):
    image = cv2.imread(imagePath)
    oldHeight, oldWidth = image.shape[:2]
    if max([oldHeight, oldWidth]) > maxValue:
        if oldHeight >= oldWidth:
            newHeight = maxValue
            newWidth = int(oldWidth * (maxValue / oldHeight))
        else:
            newWidth = maxValue
            newHeight = int(oldHeight * (maxValue / oldWidth))
        res_img = cv2.resize(image,(newWidth, newHeight), interpolation = cv2.INTER_AREA)
        cv2.imwrite(imagePath,res_img)

# write File or Directory name to a txt file
# flag: 0 is directory, 1 is file
def writeToTxt(path, txtPath, flag = 0):
    with open(txtPath, 'w') as fw:
        contents = [x for x in os.listdir(path)]
        contents = sorted(contents)
        for idx, content in enumerate(contents):
            content = str(content) + ' ' + str(idx) + '\n'
            fw.writelines(content)
# copy src file to dest file    
def copyFile(src, dst):
    dirs = [x for x in os.listdir(src)]
    dirs = sorted(dirs)
    for idx, name in enumerate(dirs):
        imageDir = os.path.join(src, name)
        images = [x for x in os.listdir(imageDir)]
        for n,img in enumerate(images):
            imgPath = os.path.join(imageDir, img)
            dstImagePath = os.path.join(dst,*(name,img))
            shutil.copyfile(imgPath, dstImagePath)
            

if __name__ == '__main__':
    rootPath = '/home/cai/dataset/foodIngredients/'
    folder_path = '/home/cai/dataset/foodIngredients/images/'
    txtFile = folder_path + 'camera_classes.txt'
    labelTxtPath = folder_path + 'camera_label.txt'
    
    dir2 = folder_path + 'total_trainImages/'     
    dir1 = folder_path + 'camera_trainImages/'
    dir3 = folder_path + 'trainImages/'    
    copyFile(dir3, dir2)