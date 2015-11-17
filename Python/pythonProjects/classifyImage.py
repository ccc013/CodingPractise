# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:01:19 2015

@author: cai
"""
from __future__ import print_function
import numpy as np
import matplotlib.pylab as plt
import os
from sklearn.externals import joblib
import time

startTime = time.ctime()
start = time.time()

rootPath = '/home/cai/'
caffe_root = rootPath + 'caffe/'
myDataPath = rootPath + 'dataset/foodIngredients/'
trainedModelPath = myDataPath + 'trainModels/train_256_total/foodIngredientsNet_train_iter_50000.caffemodel'
netParmasPath = myDataPath + 'models/deploy.prototxt'
meanFilePath = caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy'
labelFilePath = myDataPath + 'images/camera_labels.txt'
svmModelPath = myDataPath + 'examples/_temp/total_features_libsvm/svmModelsOneVsRest/svmTrainModel.pkl'

import sys
sys.path.insert(0, caffe_root + 'python')
import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

if not os.path.isfile(trainedModelPath):
    print("cannot find the file %s" % trainedModelPath)
if not os.path.isfile(netParmasPath):
    print("cannot find the file %s" % netParmasPath)

# GPU mode    
caffe.set_device(0)    
caffe.set_mode_gpu()

net = caffe.Net(netParmasPath, trainedModelPath, caffe.TEST)

transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0,1))
transformer.set_mean('data', np.load(meanFilePath).mean(1).mean(1)) # mean pixel
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))

net.blobs['data'].reshape(1, 3, 227, 227)

# classify one image
testImagesPath = myDataPath + 'web_testImages'
classifyLogTxtFile = os.path.join(myDataPath, 'classifyLog.txt')
imageNames = [x for x in os.listdir(testImagesPath)]
imageNames = sorted(imageNames)
totalNums = len(imageNames)
print('image nums is {0}'.format(totalNums))
correctNums = 0
fw = open(classifyLogTxtFile, 'w')
for name in imageNames:
    imagePath = os.path.join(testImagesPath, name)
    
    net.blobs['data'].data[...] = transformer.preprocess('data', 
                                        caffe.io.load_image(imagePath))
    out = net.forward()
    features = net.blobs['fc7'].data
    #print(len(features))
    
    # load the SVM trained Model
    clf = joblib.load(svmModelPath)
    
    predict = clf.predict(features)
    predict = predict.astype(int)
    
    #print('SVM--predicted class is #%d' % (predict[0]))
    
    with open(labelFilePath,'r') as f:
        line = f.readlines()
        idx = predict[0]
        p_label = line[idx].strip()
        true_label = name.split('_')[0]
        #print('image--{imgName}'.format(imgName = name))
        #print('SVM--predicted class {0}'.format(p_label))
        #print('true class #{0}'.format(true_label))
        fw.write('image--{imgName}'.format(imgName = name) + '\n')
        fw.write('SVM--predicted class {0}'.format(p_label) + ' ' + 'true class #{0}'.format(true_label))
        fw.write('\n')
        if int(idx) == int(true_label):
            correctNums += 1
        else:
            print('image--{imgName}'.format(imgName = name))
            print('SVM--predicted class {0}'.format(p_label))
            print('true class #{0}'.format(true_label))
            
print('correct predict nums is {0}'.format(correctNums))
print('accuracy is {0}'.format((correctNums * 1.0 / totalNums)))
fw.close()
end = time.time()
endTime = time.ctime()
print("start at %s\nend at %s" % (startTime, endTime))
print("total use %s seconds" % (end - start))