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
import shutil,math

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

def rotate_about_center(srcPath,angle,scale=1):
    src = cv2.imread(srcPath)
    w = src.shape[1]
    h = src.shape[0]
    # 角度变弧度
    rangle = np.deg2rad(angle)
    # 计算新图片的宽和高
    nw = (abs(np.sin(rangle)*h)+abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h)+abs(np.sin(rangle)*w))*scale
    print('nw={0},nh={1}'.format(nw,nh))
    # 获得旋转矩阵
    rot_mat = cv2.getRotationMatrix2D((nw*0.5,nh*0.5),angle,scale)
    print('rot_mat',rot_mat)
    # 计算从旧中心点移动到新的中心点的距离
    rot_move = np.dot(rot_mat,np.array([((nw-w)*0.5,(nh-h)*0.5),0]))
    print('rot_move',rot_move)
    rot_mat[0,2] += rot_move[0]
    rot_mat[1,2] += rot_move[1]
    return cv2.warpAffine(src,rot_mat,(int(math.ceil(nw)),int(math.ceil(nh))),
                          flags=cv2.INTER_LANCZOS4)

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

# 获取一个指定长度和随机数范围的列表,mode=0,表示取值可以重复，mode=1表示取值不重复
def getRandIntListWithoutRepetition(low,height,size,mode=1):
    results=[]
    a = np.random.randint(low,height,size)
    results = list(a)
    if mode == 0:
        return results
    for i in range(size):
        if results.count(a[i]) > 1:
            getRandIntListWithoutRepetition(low,height,size,mode)
    
    return results
    
        
# 生成训练集和测试集，可以修改函数中训练集和测试集的文件夹路径
#   filePath：原始数据集的文件路径
def generateTrainOrTestCollection(filePath):
    filelists = [x for x in os.listdir(filePath)]
    filelists = sorted(filelists)
    #random.shuffle(filelists)
    for _dir in filelists:
        imageDirPath = os.path.join(filePath,_dir)
        dirs = [x for x in os.listdir(imageDirPath)]
        random.shuffle(dirs)
        lens = len(dirs)
        trainNums = 30
        #train_array = getRandIntListWithoutRepetition(0,lens,30,1)
        print(_dir)
        #tests=[]
        #print(train_array)
        #print('trainNums: ',trainNums)
        for idx, _file in enumerate(dirs):
            path = os.path.join(imageDirPath, _file.strip())
            
        #if os.path.isfile(path):
             # split the image to train and test set 
            try:
                img = Image.open(path)
            except IOError as e:
                print('can not open :', path)
                print('error: ',e)
            #print('processing',path)
            imagelist = path.split('/')
            trainImagePath = os.path.join(root_Path,'images/trainImages','train3',imagelist[-2],_file.strip())
            testImagePath = os.path.join(root_Path,'images/testImages','test3',imagelist[-2],_file.strip())
            # 如果文件已经存在则跳过
            if os.path.isfile(trainImagePath) or os.path.isfile(testImagePath):
                continue
            if idx < trainNums:
                #content = imagelist[-1].split('_')[1].split('.')[0]
                #tests.append(content)
                print('start copy to ',trainImagePath)
                shutil.copyfile(path,trainImagePath)
            else:
                print('start copy to ',testImagePath)                 
                shutil.copyfile(path,testImagePath)
        #break
        #elif os.path.isdir(path):
            #generateTrainOrTestCollection(path)

# 数据拓展,可以修改函数中用来拓展数据的方法，默认是使用flipImage()这个方法进行水平或垂直翻转图片
# classTxtFile: 保存类名字的文件       imagePath:图像的总路径
def data_argumentation(classTxtFile,imagePath):
    for root,dirs,files in os.walk(imagePath):
        for _dir in dirs:
            imageDirs = os.path.join(imagePath,_dir)
            print(imageDirs)
            imageNames = [ x for x in os.listdir(imageDirs)]
            imageNames = sorted(imageNames)
            for img in imageNames:
                image = os.path.join(imageDirs,img)
                print(image)
                rot_angle = random.randint(0,45)
                #print(rot_angle)
                newImage_rotate = rotateImagebyCV(image,rot_angle)#rotate_about_center(image,45,1)
                newPath = image.split('.')[0] + '_rotate'+str(rot_angle)+'.jpg'
                cv2.imwrite(newPath,newImage_rotate)
            
                newImage_flip = flipImage(image,1)
                newPath = image.split('.')[0] + '_rotateBottom.jpg'
                newImage_flip.save(newPath)
    
    
# 生成训练和测试集的标签文件,可以根据需要修改标签文件的内容
# classTxtFile: 保存类名字的文件； 
# trainDirPath: 训练集文件路径；  testDirPath: 测试集文件路径
def generateTrainOrTestLabelFile(classTxtFile,trainDirPath,testDirPath):
    fr = open(classTxtFile, 'r')
    ftrain = open(trainTxtFile, 'w')
    ftest = open(valTxtFile, 'w')
  
    nameLists = fr.readlines()
    print(len(nameLists))
    #nameLists = sorted(nameLists)
    for label,name in enumerate(nameLists):
        
        c_name = name.split(' ')[0]
        labels = name.split(' ')[1:]
        print('processing',unicode(name))
        # 训练集和测试集的文件路径
        imageTrainDirPath = os.path.join(trainDirPath,'train1', c_name.strip())
        imageTestDirPath = os.path.join(testDirPath,'test1', c_name.strip())
        names_train = [x for x in os.listdir(imageTrainDirPath)]
        names_train= sorted(names_train)
        
        names_test = [x for x in os.listdir(imageTestDirPath)]
        names_test=sorted(names_test)
        # 将训练集的图片路径写入训练集标签文件
        for name in names_train:
            fullname = os.path.join(imageTrainDirPath, name)
            # 标签文件的内容
            label_str = ""
            for label in labels:
                label_str += str(label) + ' '
            label_str = label_str.strip()
            info = fullname.replace(trainDirPath, 'images/trainImages') + ' ' + label_str + '\n' 
            ftrain.write(info)
        
        # 生成测试集的标签文件
        for name in names_test:
            fullname = os.path.join(imageTestDirPath, name)
            label_str = ""
            for label in labels:
                label_str += str(label) + ' '
            label_str = label_str.strip()
            info = fullname.replace(testDirPath, 'images/testImages') + ' ' + label_str + '\n'
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
    root_Path = '/home/cai/dataset/foodIngredients-70'
    #imagePath = os.path.join(root_Path , 'Image-256')
    imagePath = os.path.join(root_Path , 'images/orginals')
    txtFilePath = os.path.join(root_Path, 'data/')
    
    classTxtFile = os.path.join(txtFilePath, 'multi_labels.txt')
    #trainDirPath = os.path.join(root_Path,'trainImages-256')
    #testDirPath = os.path.join(root_Path,'testImages-256')
    trainDirPath = os.path.join(root_Path,'images/trainImages')
    testDirPath = os.path.join(root_Path,'images/testImages')
    
    trainTxtFile = os.path.join(txtFilePath,'train_meta_256_f1_multi2.txt')
    valTxtFile = os.path.join(txtFilePath,'val_meta_256_f1_multi2.txt')
    
    
    #data_argumentation(classTxtFile,trainDirPath)
#==============================================================================
#     name = '上海青'
#     dirPath = os.path.join(trainDirPath,name)
#     images = [x for x in os.listdir(dirPath)]
#     for img in images:
#         oldName = os.path.join(dirPath,img)
#         img = img.split('_')[1]
#         new = name + '_' + img
#         newName = os.path.join(dirPath,new)
#         #print('newName',newName)
#         os.rename(oldName,newName)
#==============================================================================
    
    
#==============================================================================
#     testTxt = os.path.join(root_Path,'test.txt')
#     name = '上海青'
#     dirPath = os.path.join(trainDirPath,name)
#     fw = open(testTxt,'w')
#     images = [x for x in os.listdir(dirPath)]
#     for img in images:
#         content = 'images/trainImages/'+name+'/'+img+" " + str(69)+"\n"
#         fw.writelines(content)
#     fw.writelines("\n")
#     dirPath = os.path.join(testDirPath,name)
#     images = [x for x in os.listdir(dirPath)]
#     for img in images:
#         content = 'images/testImages/'+name+'/'+img+" " + str(69)+"\n"
#         fw.writelines(content) 
#==============================================================================
   # fw.close()   
     
           
            
    
    # 图像灰度化处理
    #convertToGreyImage(img,new)
    
    # 数据拓展
    #data_argumentation(classTxtFile,trainDirPath)
    #data_argumentation(classTxtFile,testDirPath)
    
    # 生成训练集和测试集
    #generateTrainOrTestCollection(imagePath)
    
    # 生成训练和测试集的标签文件
    
    generateTrainOrTestLabelFile(classTxtFile, trainDirPath, testDirPath)
    
    
    # 测试写入的图片路径是否正确
    #test_image(trainTxtFile,valTxtFile,root_Path)  
    

        
