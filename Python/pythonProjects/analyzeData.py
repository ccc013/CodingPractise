# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:24:44 2016

@author: cai
"""

# 统计分析直方图变量
from __future__ import print_function
import sys,os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


reload(sys)
sys.setdefaultencoding('utf8')

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def getHist(image):
    hist = [0]*256
    h,w = image.shape
    for i in range(h):
        for j in range(w):
            intensity = int(image[i,j])
            hist[intensity] = hist[intensity]+1
    
    return hist

# 计算单个向量的均值
def calcMean(hist):
    nums = 256*256
    sums = 0
    for idx in range(256):
        sums = sums + idx * hist[idx]
    
    mean = int(sums/nums)
    return mean

# 计算多个向量的均值，输入是一个包含多个列表的列表，返回均值的列表
def calcMeans(hists):
    means = []
    for hist in hists:
        mean = calcMean(hist)
        means.append(mean)
    
    return means
    
def calcVar(hist,mean):
    sums = 0
    nums = (256*256-1)*256
    for idx in range(256):
        sums += (idx-mean)*(idx-mean)* hist[idx]
    
    var = float(sums/nums)
    return var

def calcVars(hists,means):
    Vars=[]
    for hist,mean in zip(hists,means):
        Vars.append(calcVar(hist,mean))
    
    return Vars
    
# 绘制柱状图
def plotBar(nGroups,bValue,gValue,rValue,names,title,fileName):
    index = np.arange(nGroups)
    fix, ax = plt.subplots()
    bar_width = 0.5
    
    opacity = 0.4
    
    rects1 = plt.bar(index,bValue,bar_width/2,alpha=opacity,color='b',label='blue channel')
    rects2 = plt.bar(index+bar_width/2,gValue,bar_width/2,alpha=opacity,color='g',label='green channel')
    rects3 = plt.bar(index+bar_width,rValue,bar_width/2,alpha=opacity,color='r',label='red channel')
    
    plt.xlabel(u'图片名字')
    plt.ylabel('intensity')
    plt.title(title)
    
    plt.xticks(index+bar_width/2,names,rotation=90)
    plt.legend()
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)
    
    plt.tight_layout()
    plt.show()
    plt.savefig(fileName)
    
    
# txtFile = "/home/cai/dataset/foodIngredients-70/histogramMat.txt"

dirPath = 'D:\\研究生\\Dataset\\foodIngredients-70'
# imagePath = os.path.join(dirPath , 'Image-256')
# txtFilePath = os.path.join(dirPath, 'data/')
classTxtPath = os.path.join(txtFilePath,'classTxt_256')
histogramTxtPath=os.path.join(txtFilePath,'histogram_256')
histogramPlotResultPath=os.path.join(dirPath,'plot_result/histogramPlotResult')

bHist=[]
gHist=[]
rHist=[]
   
for root,dirs,files in os.walk(classTxtPath):
    files = sorted(files)
    for _file in files:
        txtName = os.path.join(classTxtPath,_file)
        print(txtName)
        histogramPath=os.path.join(histogramTxtPath,_file)
        fw = open(histogramPath,'w')
        print(histogramPath)
        with open(txtName,'r') as fr:
            counts = 0
            names=[]
            for line in fr:
                line = line.strip()
                #print(line)
                img = cv2.imread(line)
                imgName = os.path.split(line)[1]
                names.append(imgName)
                #print(imgName)
                b,g,r = cv2.split(img)
                histB = getHist(b)
                histG = getHist(g)
                histR = getHist(r)
                bHist.append(histB)
                gHist.append(histG)
                rHist.append(histR)
                counts += 1
                #cv2.calcHist(r,[2],None,[256],[0.0,255.0])
                #print('meanB',calcMean(histB))
                #fw.writelines(line+'\n')
                #fw.writelines(str(histB)+'\n')
                #fw.writelines(str(histG)+'\n')
                #fw.writelines(str(histR)+'\n\n')
        #print(counts)
        meanB=calcMeans(bHist)
        meanG=calcMeans(gHist)
        meanR=calcMeans(rHist)
        VarB = calcVars(bHist,meanB)
        VarG = calcVars(gHist,meanG)
        VarR = calcVars(rHist,meanR)
        #print(VarB)
        #print(names)
        imgNames = os.path.split(histogramPath)[1]
        className=imgNames.split('.')[0]
        resultMeanPath = os.path.join(histogramPlotResultPath,className+'_mean.jpg')
        resultVarPath = os.path.join(histogramPlotResultPath,className+'_var.jpg')
        
        plotBar(counts,meanB,meanG,meanR,names,className+u' 均值分布',resultMeanPath)
        plotBar(counts,VarB,VarG,VarR,names,className+u' 方差分布',resultVarPath)
        fw.close()
        bHist=gHist=rHist=[]
        break
        
                
                
                
                
                