# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:32:34 2015

@author: cai
"""
from __future__ import print_function
from __future__ import division
import os,sys
import shutil

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
        #print('processing',path)
        if os.path.isfile(path):
            names = os.path.split(filePath)
            print("processing ",names[1])
            newName = names[1] +"_"+ str(idx) + _file[-4:]
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
            content = str(content) +' ' + str(idx) +'\n'
            fw.writelines(content)

# copy src file to dest file    
def copyFile(src, dst):
    dirs = [x for x in os.listdir(src)]
    dirs = sorted(dirs)
    for idx, name in enumerate(dirs):
        imageDir = os.path.join(src, name)
        images = [x for x in os.listdir(imageDir)]
        newDirName = ""
        for n in name:
            if not str.isdigit(n):
                newDirName += str(n)
        print("processing ",newDirName)
        for n,img in enumerate(images):
            imgPath = os.path.join(imageDir, img)
            dstImagePath = os.path.join(dst,*(newDirName,img))
            dstDirPath = os.path.join(dst,newDirName)
            if not os.path.isdir(dstDirPath):
                os.mkdir(dstDirPath)
            #print("processing ",dstImagePath)
            shutil.copyfile(imgPath, dstImagePath)

# count file numbers and record to a txt
def recordFileNums(dirPath,txtPath):
    with open(txtPath,'w') as fw:
        dirs = [x for x in os.listdir(dirPath)]
        dirs = sorted(dirs)
        lens = len(dirs)
        
        lessClass = 0
        totalImages = 0
        lessClassNums = []
        MoreClassNums = 0
        MoreClass = []
        for dir in dirs:
            newDirPath = os.path.join(dirPath,dir)
            files = [x for x in os.listdir(newDirPath)]
            fileLength = len(files)
            if fileLength <= 50:
                lessClass += 1
                lessClassNums.append(dir)
            else:
                totalImages += fileLength
            if fileLength >= 50:
                MoreClassNums += 1
                MoreClass.append(dir)

            content = dir + " " + str(fileLength)+"\n"
            fw.writelines(content)
        fw.writelines("class numbers = "+str(lens)+"\n")
        contents = "totalImages = "+str(totalImages)+"\n"
        fw.writelines(contents)
        fw.writelines(contents)

# 将一个文件夹中的文件路径写在txt文件中   
def writeFilePath(dirPath,txtPath):
    files = [x for x in os.listdir(dirPath)]
    names = os.path.split(dirPath)
    recordTxtPath = os.path.join(txtPath,names[1]+".txt")
   
    files = sorted(files)
    lens = len(files) 
    print("processing ",names[1],lens)
    fw = open(recordTxtPath,"w")
    for _file in files:
        filePath = os.path.join(dirPath,_file)
        fw.writelines(filePath+"\n")
    fw.close()




if __name__ == '__main__':
    rootPath = "D:\\研究生\\Dataset\\foodIngredients-70"
    dstPath = "D:\\研究生\\Dataset\\foodIngredients-70\\Images"
    srcPath = "D:\\研究生\\Dataset\\foodIngredients-70\\新建文件夹"
    
    classTxtPath = os.path.join(rootPath,"class.txt")
    recordTxtPath =os.path.join(rootPath,"record.txt")
    labelTxtPath = os.path.join(rootPath,"label.txt")
    txtDirPath = os.path.join(rootPath,"totalImagesTxt")
    trainImagePath=os.path.join(rootPath,"Images-original","trainImages")
    testImagePath=os.path.join(rootPath,"Images-original","testImages")

    #createFolder(classTxtPath,testImagePath)


    dirs=[x for x in os.listdir(testImagePath)]
    for _dir in dirs:
        imageDir = os.path.join(testImagePath,_dir)
        images = [x for x in os.listdir(imageDir)]
        for img in images:
            imagePath = os.path.join(imageDir,img)
            newImagePath = os.path.join(rootPath,"Images-original","Images",_dir,img)
            print(newImagePath)
            #print("original imagePath--",imagePath)
            shutil.copyfile(imagePath,newImagePath)
            
        

    #recordFileNums(dstPath,recordTxtPath)
    #writeToTxt(dstPath,labelTxtPath)
    #read_file(dstPath)

    #copyFile(srcPath,dstPath)


