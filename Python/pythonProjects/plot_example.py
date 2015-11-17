# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:27:20 2015

@author: cai
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.axes_grid1 import host_subplot

path = '/home/cai/dataset/foodIngredients/'
train_log = path + "caffe_train_foodIngredients_finetuning_top1.log.train"
test_log = path + "caffe_train_foodIngredients_finetuning_top1.log.test"

train_log = pd.read_csv(train_log)
test_log = pd.read_csv(test_log)


#host = host_subplot(111)#, axes_class=AA.Axes)
#plt.subplots_adjust(right=0.75)
_, host = plt.subplots(figsize=(15, 10))

par1 = host.twinx()


p1, = host.plot(train_log["NumIters"], train_log["loss"], alpha=0.4, label="training_loss")
p3, = host.plot(test_log["NumIters"], test_log["loss"], 'g', label="valdation_loss")
p2, = par1.plot(test_log["NumIters"], test_log["accuracy"], 'r', label="validation_accuracy")

host.set_xlabel("iterations")
host.set_ylabel("log loss")
par1.set_ylabel("validation accuracy")

host.legend(loc=1)
par1.legend(loc=2)

#host.axis["left"].label.set_color(p1.get_color())
#par1.axis["right"].label.set_color(p2.get_color())

#plt.draw()
#plt.show()

#==============================================================================
# _, ax1 = subplots(figsize=(15, 10))
# ax2 = ax1.twinx()
# line1 = ax1.plot(train_log["NumIters"], train_log["loss"], alpha=0.4, label = 'train_loss')
# line2 = ax1.plot(test_log["NumIters"], test_log["loss"], 'g', label = 'test_loss')
# line3 = ax2.plot(test_log["NumIters"], test_log["accuracy"], 'r', label = 'test_accuracy')
# ax1.set_xlabel('iteration')
# ax1.set_ylabel('train loss')
# ax2.set_ylabel('test accuracy')
# 
# ax1.legend(loc = 1)
# 
# ax1.axis["left"].label.set_color(line1.get_color())
# ax2.axis["right"].label.set_color(line3.get_color())
#==============================================================================

