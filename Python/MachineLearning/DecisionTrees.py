#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2016/10/27 21:48
@Author  : cai

决策树算法
"""
from math import log
import operator

# 计算给定数据集的信息熵
def calcEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有可能分类创建字典
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 1
        else:
            labelCounts[currentLabel] += 1
    Ent = 0.0
    for key in labelCounts:
        # print('key={0}, count={1}\n'.format(key, labelCounts[key]))
        prob = float(labelCounts[key]) / numEntries
        Ent -= prob * log(prob, 2)
    return Ent

# 生成自定义的数据集
def createDataSet():
    dataset = [[1, 1, 'yes'],
         [1 , 1, 'yes'],
         [1, 0, 'no'],
        [0, 1, 'no'],
         [ 0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataset, labels

# 按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

# 选择最好的特征划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcEnt(dataSet)
    # 信息增益
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        # 创建唯一的分类标签列表
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            # 计算每种划分方式的信息熵
            newEntropy += prob * calcEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i

    return bestFeature

# 返回次数最多的分类名称
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 1
        else:
            classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reversed=True)
    return sortedClassCount[0][0]

# 创建决策树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # 类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        # 遍历完所有特征时返回出现次数最多的
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    # 得到列表包含的所有属性值
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


# 测试
myDat, labels = createDataSet()
Ent = calcEnt(myDat)
# print(myDat)
# print('labels=', labels)
# print('Ent=', Ent)
dat1 = splitDataSet(myDat, 0, 1)
dat2 = splitDataSet(myDat, 0, 0)
print('dataset1=', dat1)
print('dataset2=', dat2)
print('bestFeatures=', chooseBestFeatureToSplit(myDat))
myTree = createTree(myDat, labels)
print('Tree=', myTree)



