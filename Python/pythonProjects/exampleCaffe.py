# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:56:50 2015

@author: cai

an example that classify an image with the bundled CaffeNet model.
"""
import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '/home/cai/caffe/'
myDate_root = '/home/cai/dataset/foodIngredients/'
model_path = myDate_root + 'trainModels/train-256/food101net_train_iter_50000.caffemodel'
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

import os
if not os.path.isfile(caffe_root + \
    'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'):
    print("Downloading pre-trained CaffeNet model...")

if not os.path.isfile(model_path):
    print("cannot find the model")
print('classify start...')
    

# set caffe to GPU mode
caffe.set_device(0)
caffe.set_mode_gpu()

# load the net in the test phrase for reference
net = caffe.Net(myDate_root + 'models/deploy.prototxt',
                model_path,
                caffe.TEST)

# input preprocessing: 'data' is the name of the input blob == net.inputs[0]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
# mean pixel
transformer.set_mean('data', np.load(caffe_root + \
                'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1))
# the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_raw_scale('data', 255)
# the reference model has channels in BGR instead of RGB
transformer.set_channel_swap('data', (2,1,0))

# set net to batch size of 50
net.blobs['data'].reshape(50, 3, 227, 227)
net.blobs['data'].data[...] = transformer.preprocess('data', 
                                  caffe.io.load_image(myDate_root \
                                  + 'testImages/0.jpg'))
#==============================================================================
out = net.forward()
#print("Predicted class is #{}.".format(out['prob'].argmax()))

for k, v in net.params.items():
    print((k, v[0].data.shape))

#
#top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
#print(top_k)

