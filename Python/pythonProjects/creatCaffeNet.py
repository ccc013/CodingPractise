#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:58:25 2016

@author: J-Dragon

A program to generate network prototxt.
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys
import argparse
import glob
import time
import lmdb

sys.path.append("/home/cai/caffe/python")
import caffe
from caffe import layers as layer
from caffe import params as param

#def addResBlock (blockName, top, bottom, layerNum = 2):


def creatNet (trainData, traintbatchSize, trainMeanFile, testData, testbatchSize, testMeanFile):
   net = caffe.NetSpec()
   net.data, net.label = layer.Data(ntop = 2, batch_size = trainbatchSize, backend = param.Data.LMDB, source = trainData, include = dict(phase = 0), transform_param=dict(mirror=True, crop_size = 227, mean_file = trainMeanFile))
   #net.data1, net.label1 = layer.Data(ntop = 2, batch_size = testbatchSize, backend = param.Data.LMDB, source = testData, include = dict(phase = 1),  transform_param=dict(mirror=False, crop_size = 227, mean_file = testMeanFile))
	
   # conv1
   net.conv1 = layer.Convolution(net.data, num_output = 96,param = dict(lr_mult = 1,decay_mult = 1), kernel_size = 11, pad = 0,stride = 4, weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 0))
   net.relu1 = layer.ReLU(net.conv1, negative_slope = 0, in_place = True)
   net.pool1 = layer.Pooling(net.relu1, pool = param.Pooling.MAX, kernel_size = 3, stride = 2)
   net.norm1 = layer.LRN(net.pool1, local_size=5, alpha=1e-4, beta=0.75)
	#conv2 
   net.conv2 = layer.Convolution(net.norm1, group=2, num_output = 192,param = dict(lr_mult = 1,decay_mult = 1), kernel_size = 5, pad = 2, weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 1))
   net.relu2 = layer.ReLU(net.conv2, negative_slope = 0, in_place = True)
   net.pool2 = layer.Pooling(net.relu2, pool = param.Pooling.MAX, kernel_size = 3, stride = 2)
   net.norm2 = layer.LRN(net.pool2, local_size=5, alpha=1e-4, beta=0.75)
	#conv3 
   net.conv3 = layer.Convolution(net.norm2, num_output = 256,param = dict(lr_mult = 1,decay_mult = 1), kernel_size = 3, pad = 1, weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 0))
   net.relu3 = layer.ReLU(net.conv3, negative_slope=0, in_place = True)
   # conv4
   net.conv4 = layer.Convolution(net.relu3, group=2, num_output = 256,param = dict(lr_mult = 1,decay_mult = 1),kernel_size = 3, pad = 1, weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 1))
   net.relu4 = layer.ReLU(net.conv4, negative_slope = 0, in_place = True)
   # conv5
   net.conv5 = layer.Convolution(net.relu4, group=2, num_output = 192,param = dict(lr_mult = 1,decay_mult = 1), kernel_size = 3, pad = 1, weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 1))
   net.relu5 = layer.ReLU(net.conv5, negative_slope = 0, in_place = True)
   net.pool5 = layer.Pooling(net.relu5, pool = param.Pooling.MAX, kernel_size = 3, stride = 2)
   
	# fully connect layers
	#net.merge = layer.Eltwise(net.drop3, net.cccp3_1_bn, net.conv3_1_bn, net.cccp2_1_bn, net.conv2_1_bn, net.cccp1_1_bn, net.conv1_1_bn)
   net.ip1 = layer.InnerProduct(net.pool5, num_output = 2048,param = dict(lr_mult = 1,decay_mult = 1),weight_filler = dict(type = 'gaussian', std = 0.005), bias_filler = dict(type = 'constant', value = 1))
   net.relu_ip1 = layer.ReLU(net.ip1, negative_slope = 0, in_place = True)
   net.drop1 = layer.Dropout(net.relu_ip1, dropout_ratio = 0.5, in_place = True)
   net.ip2 = layer.InnerProduct(net.drop1, num_output = 4096,param = dict(lr_mult = 1,decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.005), bias_filler = dict(type = 'constant', value = 1))
   net.relu_ip2 = layer.ReLU(net.ip2, negative_slope = 0, in_place = True)
   net.drop2 = layer.Dropout(net.relu_ip2, dropout_ratio = 0.5, in_place = True)
   net.ip3 = layer.InnerProduct(net.drop2, num_output = 70, param = dict(lr_mult = 1,decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 0))
 
   net.ip1_1 = layer.InnerProduct(net.pool5, num_output = 2048, param = dict(lr_mult = 1,decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.005), bias_filler = dict(type = 'constant', value = 1))
   net.relu_ip1_1 = layer.ReLU(net.ip1_1, negative_slope = 0, in_place = True)
   net.drop1_1 = layer.Dropout(net.relu_ip1_1, dropout_ratio = 0.5, in_place = True)
   net.ip2_1 = layer.InnerProduct(net.drop1_1, num_output = 4096,param = dict(lr_mult = 1,decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.005), bias_filler = dict(type = 'constant', value = 1))
   net.relu_ip2_1 = layer.ReLU(net.ip2_1, negative_slope = 0, in_place = True)
   net.drop2_1 = layer.Dropout(net.relu_ip2_1, dropout_ratio = 0.5, in_place = True)
   net.ip3_1 = layer.InnerProduct(net.drop2_1, num_output = 70, param = dict(lr_mult = 1,decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.01), bias_filler = dict(type = 'constant', value = 0))
    
   
   #outputs 1
   net.loss = layer.SoftmaxWithLoss(net.ip3, net.label)
   net.accuracy = layer.Accuracy(net.ip3, net.label, include = dict(phase = 1))
   
   # output 2
   net.loss_2 = layer.SoftmaxWithLoss(net.ip3_1, net.label)
   net.accuracy_2 = layer.Accuracy(net.ip3_1, net.label, include = dict(phase = 1))
   
   return net.to_proto()

#if __name__=='__name__':
root_Path = '/home/cai/dataset/foodIngredients-70'
trainData = os.path.join(root_Path,'example/foodIngredients-70_train_lmdb_256_f1_multi')
testData = os.path.join(root_Path,'example/foodIngredients-70_val_lmdb_256_f1_multi')
trainMeanFile = os.path.join(root_Path,'data/foodIngredients-70_mean_train_256_f1_more.binaryproto')
testMeanFile = os.path.join(root_Path, 'data/foodIngredients-70_mean_val_256_f1.binaryproto')
testbatchSize = 50
trainbatchSize = 128
with open("/home/cai/dataset/foodIngredients-70/model/multiLabel.prototxt", 'w') as fw:
	fw.write(str(creatNet(trainData, trainbatchSize,trainMeanFile, testData, testbatchSize, testMeanFile)))

