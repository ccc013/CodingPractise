#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 1 13:58:25 2015

@author: J-Dragon

A program to generate LMDB for training.
"""

import os
import sys
import random
import cv2
import shutil
import lmdb
import numpy as np

sys.path.append("/home/yang/caffe-master/python")
import caffe

lmdb_path = '/home/yang/caffe-fractionalmaxpooling/examples/mnist/mnist_test_lmdb'
lmdb_name = 'resize_mnist_test_lmdb'
SavePath = '/home/yang/caffe-fractionalmaxpooling/examples/mnist/'
#pad = 5
resize_h = 36
resize_w = 36

## Open the lmdb file ##
lmdb_env = lmdb.open(lmdb_path)
lmdb_txn = lmdb_env.begin()
lmdb_cursor = lmdb_txn.cursor()
## Open the lmdb file ##

#Create LMDB
print 'Begin resizing........'
count = 0
LMDBPath = os.path.join(SavePath, lmdb_name)
if os.path.exists(LMDBPath):
	shutil.rmtree(LMDBPath)
train_db = lmdb.open(LMDBPath, map_size = int(1e10))
with train_db.begin(write = True) as in_datum:
	for key, value in lmdb_cursor:
		datum = caffe.proto.caffe_pb2.Datum()
		datum.ParseFromString(value)
		label = datum.label
		#print datum.channels, datum.height, datum.width
		image = caffe.io.datum_to_array(datum)
		image = image[0, :, :]
		height, width = image.shape
		#image = image.astype(np.float32)       #image has the format as [channel, height, width]
		# print type(image[0][0]), image.shape, label
		# cv2.imshow('ss', image)
		# cv2.waitKey(0)
		# assert 0

		new_image = cv2.resize(image, (resize_w, resize_h))
		transf = np.zeros((1, resize_h, resize_w), dtype = np.uint8)
		# print type(new_image[0][0]), new_image.shape, label
		# cv2.imshow('ss', new_image)
		# cv2.waitKey(0)
		# assert 0
		#new_image = np.zeros((height+ pad * 2, width + pad * 2), dtype = np.uint8)
		#new_image[pad: pad + height, pad : pad + width] = image
		#transf = np.zeros((1, height+ pad * 2, width + pad * 2), dtype = np.uint8)
		transf[0,:,:] = new_image

		new_datum = caffe.io.array_to_datum(transf, label=int(label))
		in_datum.put(key, new_datum.SerializeToString())

		if count%500 == 0:
			print str(count) + ' padded. '
		count = count + 1
train_db.close()

print '\nFinished padding data. Totally ' + str(count) + ' images padded. '