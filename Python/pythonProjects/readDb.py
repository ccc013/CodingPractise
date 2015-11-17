# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:01:17 2015

@author: cai
"""

import caffe
import lmdb
import os
import caffe.proto.caffe_pb2
from caffe.io import datum_to_array

root_Path = '/home/cai/dataset/foodIngredients/'
lmdb_path = root_Path + 'examples/_temp/val_features/'

lmdb_env = lmdb.open(lmdb_path)
numSamples = int(lmdb_env.stat()['entries'])
print('numSamples: ', numSamples)
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
datum = caffe.proto.caffe_pb2.Datum()

txt = root_Path + 'examples/_temp/test_features_fc7_fromLmdb.txt'
fr = open(txt, 'w')
count = 1
for key, value in lmdb_cursor:
    datum.ParseFromString(value)
    label = datum.label
    print 'count, label', (count, label)
    count += 1
    data = datum_to_array(datum)
    print len(data)
    
    for i in range(0, len(data)):
        
        info  = str(i + 1 ) + ': ' + str(data[i]) + ' '
        fr.write(info)
    fr.write('\n')

#fr.close()
print 'done!'


