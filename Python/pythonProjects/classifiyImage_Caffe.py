# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 17:59:39 2015

@author: cai
"""

import caffe
import sys

caffe_root = '/home/cai/caffe/'
myDate_root = '/home/cai/dataset/foodIngredients/'
modelDefinition_path = myDate_root + 'models/deploy.prototxt'
pre_model_path = myDate_root + 'trainModels/train-256/food101net_train_iter_50000.caffemodel'
testImagePath = myDate_root + 'testImages/4.jpg'

sys.path.insert(0, caffe_root + 'python')

net = caffe.Classifier(modelDefinition_path, pre_model_path)
net.set_phase_test()
net.set_mode_gpu()

scores = net.predict(testImagePath)
print('predict class is #', scores)
