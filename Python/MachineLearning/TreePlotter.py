#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2016/10/28 19:59
@Author  : cai

使用 matplotlib 库来绘制树形图
"""
import matplotlib.pyplot as plt

# 定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

# 绘制带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                           xytext=centerPt, textcoords='axes fraction',
                           va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.show()

# 获取叶结点的数目
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()
    # print(firstStr)
    firstStr = list(firstStr)
    secondDict = myTree[firstStr[0]]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            # 测试结点的数据类型是否为字典
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs

# 获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

# 输出预先存储的树信息
def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0:{'head': {0: 'no', 1: 'yes'}},1: 'no'}}}}
                   ]
    return listOfTrees[i]

# createPlot()
tree1 = retrieveTree(1)
print(tree1)
myTree = retrieveTree(0)
print('leafs = ', getNumLeafs(myTree))
print('depth = ', getTreeDepth(myTree))
