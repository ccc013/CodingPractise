# coding:utf8
# k-近邻算法的代码实现
# 导入科学计算包Numpy，和运算符模块

from numpy import *
import operator 

def createDataSet():
	'''
	用于创建数据集和标签
	'''
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels

def classify0(inX,dataSet,labels,k):
	'''
	k-近邻算法的代码实现
	inx:用于分类的输入向量
	dataSet：输入的训练样本集
	labels：标签向量
	k：用于选择最近邻居的数目
	采用欧氏距离公式
	'''
	dataSetSize = dataSet.shape[0] #获取输入训练样本集的维度，也是行数
	diffMat = tile(inX,(dataSetSize,1)) - dataSet  #tile函数用于扩充数组元素，所以是重复1次输入向量，执行次数是dataSetSize，然后与样本集相减得到两个向量点的距离
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5 #得到输入向量和样本集向量的距离
	sortedDistIndicies = distances.argsort() #argsort函数返回的是数组值从小到大的索引值
	classCount = {}
	for i in range(k): #统计前k个点所在类别的出现频率
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1

	#使用operator的itemgetter方法按照第二个元素的次序进行排序，并且排序为逆序，即从大到小排序，最后返回频率最高的标签
	sortedClassCount = sorted(classCount.iteritems(),
						key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]