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

sys.path.append("/home/yang/caffe-droplayer/python")
import caffe
from caffe import layers as layer
from caffe import params as param

#def addResBlock (blockName, top, bottom, layerNum = 2):


def creatNet (trainData, traintbatchSize, testData, testbatchSize):
	net = caffe.NetSpec()
	net.data, net.label = layer.Data(ntop = 2, batch_size = trainbatchSize, backend = param.Data.LMDB, source = trainData, include = dict(phase = 0))
	#net.data, net.label = layer.Data(ntop = 2, batch_size = testbatchSize, backend = param.Data.LMDB, source = trainData, include = dict(phase = 1))
	#group 1 
	net.conv1 = layer.Convolution(net.data, group_id = 1, group_prob = 0.05, num_output = 64, kernel_size = 3, pad = 1, weight_filler = dict(type = 'gaussian', std = 0.05), bias_filler = dict(type = 'constant', value = 0))
	net.relu1 = layer.ReLU(net.conv1, group_id = 1, negative_slope = 0.333, in_place = True)
	net.conv1_1 = layer.Convolution(net.relu1, group_id = 1, num_output = 256, kernel_size = 8, stride = 8)
	net.conv1_1_bn = layer.BatchNorm(net.conv1_1, use_global_stats = False)
	#group 2
	net.cccp1 = layer.Convolution(net.relu1, group_id = 2, group_prob = 0.05, num_output = 64, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = 'gaussian', std = 0.05), bias_filler = dict(type = 'constant', value = 0))
	net.relu_cccp1 = layer.ReLU(net.cccp1, group_id = 2, negative_slope = 0.333, in_place = True)
	net.cccp1_1 = layer.Convolution(net.cccp1, group_id = 2, num_output = 256, kernel_size = 8, stride = 8)
	net.cccp1_1_bn = layer.BatchNorm(net.cccp1_1, use_global_stats = False)
	#group 3
	net.pool1 = layer.Pooling(net.relu_cccp1, group_id = 3, group_prob = 0.05, pool = param.Pooling.AVE, kernel_size = 2, stride = 2)
	net.drop1 = layer.Dropout(net.pool1, group_id = 3, dropout_ratio = 0.25, in_place = True)
	net.conv2 = layer.Convolution(net.drop1, group_id = 3, num_output = 128, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu2 = layer.ReLU(net.conv2, group_id = 3, negative_slope = 0.333, in_place = True)
	net.conv2_1 = layer.Convolution(net.relu2, group_id = 3, num_output = 256, kernel_size = 4, stride = 4)
	net.conv2_1_bn = layer.BatchNorm(net.conv2_1, use_global_stats = False)
	#group 4
	net.cccp2 = layer.Convolution(net.relu2, group_id = 4, group_prob = 0.05, num_output = 128, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu_cccp2 = layer.ReLU(net.cccp2, group_id = 4, negative_slope = 0.333, in_place = True)
	net.cccp2_1 = layer.Convolution(net.relu_cccp2, group_id = 4, num_output = 256, kernel_size = 4, stride = 4)
	net.cccp2_1_bn = layer.BatchNorm(net.cccp2_1, use_global_stats = False)	
	#group 5
	net.pool2 = layer.Pooling(net.relu_cccp2, group_id = 5, group_prob = 0.25, pool = param.Pooling.AVE, kernel_size = 2, stride = 2)
	net.drop2 = layer.Dropout(net.pool2, group_id = 5, dropout_ratio = 0.25, in_place = True)
	net.conv3 = layer.Convolution(net.drop2, group_id = 5, num_output = 256, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu3 = layer.ReLU(net.conv3, group_id = 5, negative_slope = 0.333, in_place = True)
	net.conv3_1 = layer.Convolution(net.relu3, group_id = 5, num_output = 256, kernel_size = 2, stride = 2)
	net.conv3_1_bn = layer.BatchNorm(net.conv3_1, use_global_stats = False)
	#group 6
	net.cccp3 = layer.Convolution(net.relu3, group_id = 6, group_prob = 0.25, num_output = 256, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu_cccp3 = layer.ReLU(net.cccp3, group_id = 6, negative_slope = 0.333, in_place = True)
	net.cccp3_1 = layer.Convolution(net.relu_cccp3, group_id = 6, num_output = 256, kernel_size = 2, stride = 2)
	net.cccp3_1_bn = layer.BatchNorm(net.cccp3_1, use_global_stats = False)
	#group 7
	net.cccp4 = layer.Convolution(net.relu_cccp3, group_id = 7, group_prob = 0.3, num_output = 256, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu_cccp4 = layer.ReLU(net.cccp4, group_id = 7, negative_slope = 0.333, in_place = True)
	net.cccp5 = layer.Convolution(net.relu_cccp4, group_id = 7, num_output = 256, kernel_size = 3, pad = 1, param = dict(lr_mult = 1, decay_mult = 1), weight_filler = dict(type = "gaussian", std = 0.05), bias_filler = dict(type = "constant", value = 0))
	net.relu_cccp5 = layer.ReLU(net.cccp5, group_id = 7, negative_slope = 0.333, in_place = True)
	net.pool3 = layer.Pooling(net.relu_cccp5, group_id = 7, pool = param.Pooling.AVE, stride = 2, kernel_size = 2)
	net.drop3 = layer.Dropout(net.pool3, group_id = 7, dropout_ratio = 0.25, in_place = True)
	#share
	net.merge = layer.Eltwise(net.drop3, net.cccp3_1_bn, net.conv3_1_bn, net.cccp2_1_bn, net.conv2_1_bn, net.cccp1_1_bn, net.conv1_1_bn)
	net.ip1 = layer.InnerProduct(net.merge, num_output = 1024, param = dict(lr_mult = 1), weight_filler = dict(type = 'xavier'), bias_filler = dict(type = 'constant'))
	net.relu_ip1 = layer.ReLU(net.ip1, negative_slope = 0.333, in_place = True)
	net.drop4 = layer.Dropout(net.relu_ip1, dropout_ratio = 0.5, in_place = True)
	net.ip2 = layer.InnerProduct(net.drop4, num_output = 1024, param = dict(lr_mult = 1), weight_filler = dict(type = 'xavier'), bias_filler = dict(type = 'constant'))
	net.relu_ip2 = layer.ReLU(net.ip2, negative_slope = 0.333, in_place = True)
	net.drop5 = layer.Dropout(net.relu_ip2, dropout_ratio = 0.5, in_place = True)
	net.ip3 = layer.InnerProduct(net.drop5, num_output = 10, param = dict(lr_mult = 1), weight_filler = dict(type = 'xavier'), bias_filler = dict(type = 'constant'))
	#outputs
	net.loss = layer.SoftmaxWithLoss(net.ip3, net.label)
	net.accuracy = layer.Accuracy(net.ip3, net.label, include = dict(phase = 1))
	return net.to_proto()

#if __name__=='__name__':
trainData = 'examples/Drop/train_db'
testData = 'examples/Drop/val_db'
testbatchSize = 20
trainbatchSize = 128
with open("/home/yang/14new.prototxt", 'w') as fw:
	fw.write(str(creatNet(trainData, trainbatchSize, testData, testbatchSize)))

