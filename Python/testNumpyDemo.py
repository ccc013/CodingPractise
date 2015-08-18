# coding:utf8
# 测试Numpy

import numpy as np

matX = np.arange(100).reshape((10,10)) #生成一个10*10的矩阵，矩阵值是从0-99
arrayY = np.random.rand(4,4)		   #生成一个4*4的随机数组
matY = np.mat(arrayY) 				   #mat()函数可以将数组转化为矩阵
invMatY = matY.I                       #矩阵求逆
matEye = matY * invMatY				   #矩阵和其逆矩阵相乘得到单位矩阵
myEye = np.eye(4)					   #eye()函数可以生成单位矩阵

print 'matX = ',matX
print 'arrayY = ',arrayY
print 'matY = ',matY
print 'invMatY = ',invMatY
print 'matEye = ',matEye
print 'myEye = ',myEye

row = matX[3] #矩阵的第4行

col = matX[:,3] #矩阵的第4列

print 'row = ',row
print 'col = ',col