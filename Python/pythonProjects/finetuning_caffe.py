# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:22:14 2015

@author: cai
"""

import os

import sys
caffe_root = '/home/cai/caffe/'
myData_root = '/home/cai/dataset/food-101/'

os.chdir(myData_root)

sys.path.insert(0, caffe_root +'python')
sys.path.insert(1, myData_root)

import caffe
import numpy as np
from pylab import *

# iteration nums
niter = 200

# losses will also stored in the log
train_loss = np.zeros(niter)
scratch_train_loss = np.zeros(niter)

caffe.set_device(0)
caffe.set_mode_gpu()

# We create a solver that fine-tunes from a previously trained network
solver = caffe.SGDSolver(myData_root + 'models/solver.prototxt')
solver.net.copy_from(caffe_root + 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel')

# For reference, we also create a solver that does no finetuning
#scratch_solver = caffe.SGDSolver(myData_root + 'models/solver.prototxt')

# We run the solver for niter times, and record the training loss.
for it in range(niter):
    solver.step(1)   # SGD by Caffe
#==============================================================================
#     scratch_solver.step(1)
#==============================================================================
    
    # store the train loss
    train_loss[it] = solver.net.blobs['loss'].data
    #scratch_train_loss[it] = scratch_solver.net.blobs['loss'].data
    if it % 10 == 0:
        print 'iter %d, finetune_loss = %f' % (it, train_loss[it])
plot(np.vstack([train_loss]).T)

# Test
test_iters = 10
accuracy = 0
for it in range(test_iters):
    solver.test_nets[0].forward()
    accuracy += solver.test_nets[0].blobs['accuracy'].data
accuracy /= test_iters
print 'Accuracy for fine-tuning:', accuracy

print 'done'



