# coding:utf8
# 测试Numpy

import numpy as np

x = np.arange(100).reshape((10,10)) #生成一个10*10的矩阵，矩阵值是从0-99

print x

row = x[3] #矩阵的第4行

col = x[:,3] #矩阵的第4列

print 'row = ',row
print 'col = ',col