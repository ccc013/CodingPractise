# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:15:03 2016

@author: cai
输出测试图片经过前向计算后指定层的特征图结果
"""
from __future__ import print_function
import numpy as np
import lmdb
import os,sys
from PIL import Image

BATCH = 100
rootPath = '/home/cai/'
caffe_root = rootPath + 'caffe/'
sys.path.insert(0, caffe_root + 'python')
import caffe
from caffe.proto import caffe_pb2
myDataPath = os.path.join(rootPath,'dataset/foodIngredients-70/')

model_file = os.path.join(myDataPath, 'model/deploy_centerLoss_3Layers.prototxt')
weight_file = os.path.join(myDataPath, 
'trainedModel/trainNet_256More_xavier/foodIngredientsNet_train_f1_centerLoss_3Layers2_iter_30000.caffemodel')
lmdb_file = os.path.join(myDataPath, 'example/foodIngredients-70_val_lmdb_256_f1')
logFile = os.path.join(myDataPath, 'features_center2.log')
fw = open(logFile, 'w')

n = caffe.Net(model_file, weight_file, caffe.TEST)
input_name = n.inputs[0]
#print("input_name = ",input_name)
#transformer = caffe.io.Transformer({input_name: n.blobs[input_name].data.shape});
#transformer.set_input_scale(input_name, 255.0)
transformer = caffe.io.Transformer({'data':n.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
#transformer.set_mean('data', mu) # mean pixel
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))
#n.blobs['data'].reshape(50, 3, 227, 227)

lmdb_env = lmdb.open(lmdb_file)
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe_pb2.Datum()

count = 0
iters = 0
batch_data = []
batch_label = []
for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    label = datum.label
    data = caffe.io.datum_to_array(datum)
    
    im = data.astype(np.uint8)
    # array to image
    img = Image.fromarray(im, 'RGB')
    img.save('test.png')
    break
    count += 1
    batch_data.append(im)
    batch_label.append(label)
    if count % 50 == 0:
        data = np.array(batch_data, dtype=np.float32) / 255.0      
        #print(data.shape)
        n.forward_all(**{input_name: data})
        res_data = n.blobs['fc6'].data
        for res, label in zip(res_data, batch_label):
            featStr = [str(f) for f in res]
            #print str(label) + '\t' + '\t'.join(featStr)
            
            fw.writelines(str(label) + '\t' + '\t'.join(featStr)+'\n')
        iters += 1
        print('iters ', iters)
        batch_data = []
        batch_label = []

fw.close()

