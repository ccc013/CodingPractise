# -*- coding: utf-8 -*-

# 绘制柱状图

import numpy as np
import matplotlib.pyplot as plt
import sys,os,string
from imp import reload
from PIL import Image


if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.rcParams.update({'font.size': 18})

def check_contain_chinese(check_str):
	for ch in check_str:
		if u'\u4e00' <= ch <= u'\u9fff':
			return True
	return False

def plotBar(values,nums,names):
	fix, ax = plt.subplots()
	index = np.arange(nums)
	bar_width = 0.4

	opacity = 0.4
	

	# for i in range(nums):
	# 	plt.bar(index+bar_width*i*(1/128),values[i],bar_width/256,
	# 		alpha=opacity,color='g')
	
	rects1 = plt.bar(index,values[0],bar_width/3,alpha=opacity,color='b',label='蓝色通道')
	rects2 = plt.bar(index+bar_width/2,values[1],bar_width/3,alpha=opacity,color='g',label='绿色通道')
	rects3 = plt.bar(index+bar_width,values[2],bar_width/3,alpha=opacity,color='r',label='红色通道')

	# plt.bar(index+bar_width/2,values,bar_width,alpha=opacity,color='b')

	plt.xlabel('类名',fontsize = 40)
	plt.ylabel('偏度',fontsize = 40)
	# plt.title('70类食材的每类图片的直方图偏度分布')

	plt.xticks(index+bar_width/128,names,rotation=90)
	# plt.ylim(0,100000)
	plt.legend()
	ax.xaxis.grid(True)
	ax.yaxis.grid(True)

	plt.tight_layout()
	plt.show()

def plotLine(x,y,numbers,labels):
	colors = ['r','g','b','y']
	markers=['.','o','*','D','+','s','h','x','|','_']

	for i in range(numbers):
		plt.plot(x,y[i],linewidth=3.0,color=colors[i],label=labels[i])
		plt.scatter(x,y[i],s=35,marker=markers[i])
	
	# plt.plot(x,y,linewidth=3.0,color=colors[0])#,label=labels[i]
	# plt.scatter(x,y,s=35,marker=markers[0])

	ax = plt.gca()
	plt.xlabel('迭代次数')
	plt.ylabel('识别准确率(%)')
	plt.xlim(0,30000)
	plt.ylim(0,1)
	#plt.title('')

	ax.xaxis.grid(True)
	ax.yaxis.grid(True)

	plt.legend(loc=4)
	plt.show()


dirPath = "D:\\研究生\\Dataset\\foodIngredients-70\\statisticsTxt"
rootPath = "D:\\研究生\\Dataset\\foodIngredients-70"
classTxtPath = os.path.join(rootPath,"class.txt")
imageDirPath = os.path.join(rootPath,"Images-original","Images")
#names = ['白豆腐','菜心','红薯','胡萝卜','莲藕','木耳','茄子','青瓜','丝瓜','指天椒']
names=[]
with open(classTxtPath,'r') as fr:
	for line in fr:
		names.append(line.strip())
# print(names)

# lens = []
# for name in names:
# 	imageDirName = os.path.join(imageDirPath,name)
# 	images = [x for x in os.listdir(imageDirName)]
# 	l = len(images)
# 	lens.append(l)

# plotBar(lens,70,names)

results=[]

# for name in names:
txtPath = os.path.join(dirPath,'record.txt')
# 	print(txtPath)
with open(txtPath,'r') as fr:
	lines = fr.readlines()
	line = lines[6]
		
	line = line.split('=')[1]
	contents = line[1:-3]
	contents = contents.split(',')
	lists=[]
	for c in contents:
		c = str(c).strip()
		lists.append(float(c))

	results.append(lists)

	line = lines[7]
		
	line = line.split('=')[1]
	contents = line[1:-3]
	contents = contents.split(',')
	lists=[]
	for c in contents:
		c = str(c).strip()
		lists.append(float(c))
	
	results.append(lists)

	line = lines[8]
		
	line = line.split('=')[1]
	contents = line[1:-3]
	contents = contents.split(',')
	lists=[]
	for c in contents:
		c = str(c).strip()
		lists.append(float(c))
	
	results.append(lists)

# print(results)
# testData=[]
# for i in range(256):
# 	temp = []
# 	for j in range(10):
# 		temp.append(results[j][i])
# 	testData.append(temp)

# print(len(testData))

names_tuple = tuple(names)

n_groups = 70
# n_groups = 70

plotBar(results,n_groups,names_tuple)


xValues = [i for i in range(0,30001) if i % 500 == 0]
# [100,150,200,250,300,400,500]
# [100,150,200,250,300,400,500,600,700,800,900,1000]
# [50,100,150,200,250,300,400,500]

# [2,3,4,5,6,7,8,9,10,12,15,20]
# [5,10,20,30,40,50,80,100,150,200]
# [500,1000,1500,2000,2500,3000]
# 


yValues = []
filePath = "D:\\研究生\\工作记录\\plotResult\\trainNet_256More_xavier_f1.log.test"
with open(filePath,'r') as fr:
	for line in fr:
		if line[0] != '#':
			yValues.append(line[20:28].strip())

# y1 = []
# for y in yValues:
# 	y_int = string.atoi(y)
# 	y1.append(y_int)
# print(y1)
# [87.98,88.06,88.28,88.33,87.39,87.69,87.44]  # surf_color
# [84.94,85.05,85.24,85.27,85.98,85.73,86.36]  # dsift_color
# [71.96,74.78,74.31,75.24,74.83,75.9,76.27,76.34,76.66,76.58,77.02,76.68]
# [60.68,63.95,64.4,65.42,66.82,67.28,66.91,66.65]

# [70.9,74.1,75.44,76.53,76.45,76.61,76.91,75.94,75.62,75.6,75.64,75.74]
# [89.47,88.77,88.61,89.35,88.42,88.93,88.94]
# [72.17,70.96,72.66,71.95,71.63,71.95,72.6]

x2 = [i for i in range(0,30001) if i % 1000 == 0]
y2 = []
filePath2 = "D:\\研究生\\工作记录\\plotResult\\trainNet_256More_xavier4Layers_f1.log.test"
with open(filePath2,'r') as fr:
	for line in fr:
		if line[0] != '#':
			y2.append(line[20:28].strip())

# [87.3,87.1,86.36,85.83,85.49,85.29,85.38]     # surf_color
# [84.99,85.85,86.02,85.51,86.05,85.8,85.05]	# dsift_color
# [68.22,70.74,72.06,71.37,72.82,74.55,75.65,75.44,76.15,75.95,76.93,76.58]
# [87.71,86.85,87.19,86.66,86.41,86.03,86.02]

y3 = []
filePath3 = "D:\\研究生\\工作记录\\plotResult\\trainNet_256More_xavier3Layers_f1_1.log.test"
with open(filePath3,'r') as fr:
	for line in fr:
		if line[0] != '#':
			y3.append(line[20:28].strip())

# [87.86,87.49,87.9,88.2,87.3,88.57,88.08]  # surf_color
# [84.01,83.96,84.6,84.6,84.75,84.71,85.51]	# dsift_color
# [71.76,73.8,74.8,74.43,75.19,75.97,75.95,75.58,75.97,76.1,76.03,75.78]
# [87.93,86.54,87.51,89.32,87.88,89.15,88.91]

y4 = []
filePath4 = "D:\\研究生\\工作记录\\plotResult\\trainNet_finetuning_lmdb_256_f3.txt.test"
with open(filePath4,'r') as fr:
	for line in fr:
		if line[0] != '#':
			y4.append(line[20:28].strip())

# [79.1,78.93,79.34,79.81,79.78,79.58,79.37]	# surf_color
# [70.96,72.79,72.79,73.28,73.67,73.43,73.28]	# dsift_color
# [63.25,64.94,66.47,65.1,65.21,65.76,66.36,66.2,66.47,66.51,66.96,66.95] 
# [79.1,78.93,79.34,79.81,79.78,79.58,79.37]

y = []
# y.append(y4)
x = []
x.append(xValues)
x.append(x2)

y5=[]

for v in y5:
	print(v)
# print(y2)


nums = 2

# labels=['支持向量机','随机森林','朴素贝叶斯','K-最近邻']
# labels=['RBF核函数','线性核函数','Poly核函数','Sigmoid核函数']
# labels=['两层卷积层','三层卷积层','四层卷积层','五层卷积层']
labels=['直接训练模式','预训练模式']

# plotLine(xValues,y,nums,labels)

linestyles=['-','--','-.',':']
markers=['.','o','*','D','+','s','h','x','|','_']

# for i in range(10):
# 	idx_line = i%4
# 	plt.plot(xValues,meansB[i],linewidth=2.0,
# 		color='b',linestyle=linestyles[idx_line],marker=markers[i],label=names[i])


# rects2 = plt.bar(index+bar_width/2,varG,bar_width/2,
# 	alpha=opacity,color='g',label='variance of green channel')
# rects3 = plt.bar(index+bar_width,varR,bar_width/2,
# 	alpha=opacity,color='r',label='variance of red channel')

# plt.xlabel('类别')
# plt.ylabel('均值')
# plt.title('10类食材的每类图片的蓝色通道均值分布')

#className = (u"白豆腐"，u"菜心"，u"红薯"，u"胡萝卜"，u"指天椒",u"茄子")

#plt.xticks(index+bar_width/2,names_tuple)
# plt.ylim(0,255)
# plt.legend()
# ax.xaxis.grid(True)
# ax.yaxis.grid(True)

# plt.tight_layout()
# plt.show()