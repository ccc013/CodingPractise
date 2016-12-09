# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:49:09 2016

@author: cai
可视化得到的二维特征图
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def draw(path):
    with open(path,'r') as f:
        lines = f.readlines()

    d = dict()

    for line in lines:
        sps = line.split()
        val = sps[0].split('[')[1].split(']')[0]
        label = int(val)
        if label not in d:
            d[label] = []
        pt = [float(sps[1]), float(sps[2])]
        d[label].append(pt)
    print len(d)
    color = ['blue','green','red','cyan','magenta',
        'yellow','black','white','gray','pink']
#==============================================================================
#     dst = dict()
#     for i in range(10):
#         dst[i] = d[i]
#         print str(i) + "\t" + str(len(dst[i]))
#==============================================================================
    
    for key in d:
        print str(key) + "\t" + str(len(d[key]))
        val = np.array(d[key])
        x = val[:,0]
        y = val[:,1]
        #plt.scatter(x,y, label=key, c = color[key])
        c_i = key % 10
        print(c_i)
        plt.scatter(x,y, label=key, c = color[c_i])
        

    plt.legend()
    plt.show()


if __name__ == '__main__':
    rootPath = '/home/cai/'
    myDataPath = os.path.join(rootPath,'dataset/foodIngredients-70/')
    plotTxt = os.path.join(myDataPath, 'features_center2.log')
    draw(plotTxt)


