# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 18:29:22 2015

@author: cai

a function to resize image
"""
from __future__ import print_function
from __future__ import division
import os, cv2
import time

rootPath = '/home/cai/dataset/foodIngredients/images/'
originalPath = rootPath + 'original/'
newPath = rootPath + 'resize_512/'
logTxt = rootPath + "resize_log.txt"
# 日志文件
fw = open(logTxt,'w')

# 指定特定的长宽，但不保持原来长宽比
def resizeImage(imagePath, newWidth, newHeight):
    image = cv2.imread(imagePath)
    res_img = cv2.resize(image,(newWidth, newHeight), interpolation = cv2.INTER_AREA)
    splitImagePath = os.path.splitext(imagePath)
    newImagePath = splitImagePath[0] + "_res" + splitImagePath[1]
    #print(newImagePath)    
    cv2.imwrite(newImagePath,res_img)    

# 保持长宽比，给定最大的一个长或宽
def resizeImage_Max(imagePath, maxValue):
    if os.path.splitext(imagePath)[1] == '.gif':
        print(imagePath)
        return None
    image = cv2.imread(imagePath)
    oldHeight, oldWidth = image.shape[:2]
    info = str(oldWidth) + " * " + str(oldHeight)
    fw.write("%s --> %s\n" % (imagePath, info))
    if oldHeight >= oldWidth:
        newHeight = maxValue
        newWidth = int(oldWidth * (maxValue / oldHeight))
    else:
        newWidth = maxValue
        newHeight = int(oldHeight * (maxValue / oldWidth))
    # resize
    res_img = cv2.resize(image, (newWidth, newHeight), interpolation = cv2.INTER_AREA)
    return res_img
    

# 递归读取文件，并对文件进行操作
def read_file(filePath='.'):
    filelists = [x for x in os.listdir(filePath)]
    filelists = sorted(filelists)
    for _file in filelists:
        path = os.path.join(filePath, _file)
        if os.path.isfile(path):
            pass
        elif os.path.isdir(path):
            read_file(path)

def write_file(filename, content):
    with open(filename, 'a') as f:
        f.write(content + '\n')

if __name__ == '__main__':
    ext = "_resMax.jpg"
    # 设置图片宽和高调整的一个最大值
    imageMaxValue = 512
    count = 0
    
    imageDirList = [x for x in os.listdir(originalPath)]
    imageDirList = sorted(imageDirList)
    lens = len(imageDirList)
    startTime = time.ctime()
    print("start resize, time is %s" % startTime)
    fw.write("start resize, time is %s\n" % startTime)
    for i in range(lens):
        imageFilePath = originalPath + imageDirList[i] + '/'
        #print(imageDirList[i])
        imageFileList = [x for x in os.listdir(imageFilePath)]
        imageFileList = sorted(imageFileList)
        print("resizing the %s..." % unicode(imageDirList[i]))
        for idx,image in enumerate(imageFileList):
            imagePath = imageFilePath + image
            resImg = resizeImage_Max(imagePath, imageMaxValue)
            if resImg is not None:
                newImagePath = imageFilePath.replace("original","resize_512") + str(idx) + ext
                count += 1
                cv2.imwrite(newImagePath, resImg)
                info = str(resImg.shape[1]) + " * " + str(resImg.shape[0])
                fw.write("==> %s --> %s\n" % (newImagePath, info))
                print("finish %d..." % count)
          
    
    endTime = time.ctime()
    print("finish time is %s" % endTime)
    print("total process %d images." % count)
    fw.write("finish time is %s\n" % endTime)   
    fw.write("total process %d images.\n" % count)
    fw.close()    
