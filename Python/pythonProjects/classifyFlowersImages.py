# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 09:01:19 2015

@author: cai

classify flowers102 dataset use caffe
"""
from __future__ import print_function
import numpy as np
import matplotlib.pylab as plt
import os
from sklearn.externals import joblib
import time
from skimage import io; 
io.use_plugin('matplotlib')

startTime = time.ctime()
start = time.time()

rootPath = '/home/cai/'
caffe_root = rootPath + 'caffe/'
myDataPath = os.path.join(rootPath,'dataset/flowers/')
trainedModelPath = os.path.join(myDataPath,
'trainedModels/train_fc512/flowers106net_finetuning_iter_30000.caffemodel')
#==============================================================================
# trainedAlexNetModelPath=os.path.join(caffe_root,
# 'models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel')
#==============================================================================

netParmasPath = myDataPath + 'models/deploy.prototxt'

meanFilePath = myDataPath + 'data/flowers106_mean_train.npy'
#meanFilePath1 =os.path.join(caffe_root,'python/caffe/imagenet/ilsvrc_2012_mean.npy')

#labelFilePath = myDataPath + 'data/labels.txt'
#classFilePath = os.path.join(myDataPath,"data/class.txt")
testImagesPath = os.path.join(myDataPath ,'data/test_meta_106.txt')
#classifyImagePath=os.path.join(myDataPath,"classifyImages")
#svmModelPath = myDataPath + 'examples/_temp/total_features_libsvm/svmModelsOneVsRest/svmTrainModel.pkl'

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
mu = np.load(meanFilePath).mean(1).mean(1)
#print('mean-subtracted values:', zip('BGR', mu))

transformer = caffe.io.Transformer({'data':net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', mu) # mean pixel
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2,1,0))

#net.blobs['data'].reshape(1, 3, 227, 227)

# read all label name
#with open(classFilePath,'r') as fr:
#    classNameLists = fr.readlines()


# classify one image

classifyLogTxtFile = os.path.join(myDataPath, 'classifyLogs_fc512_106.txt')
# read all test image file and labels
labels = []
testImages = []
with open(testImagesPath,'r') as fr:
    contents = fr.readlines()
    for line in contents:
        splits = line.strip().split(' ')
        testImages.append(splits[0])
        labels.append(splits[1])

# predict result, record the predict class for every class
predictResults = {}
classNums = 106
for i in range(classNums):
    predictResults[i] = [0]*classNums

correctNums = 0
top5 = 0
totalNums = len(testImages)
print("testImages numbers is {0}".format(totalNums))
# record the class numbers whose accuracy is 100%
correctClass = 0
fw = open(classifyLogTxtFile, 'w')
# already predict numbers
curNums = 0
for idx,name in enumerate(testImages):
    curLabel = int(labels[idx])
    #fw.write("current label is " + str(curLabel) + "\n")
    imagePath = os.path.join(myDataPath, name)
    
    image = caffe.io.load_image(imagePath)
            
    transformed_image = transformer.preprocess('data',image)
    #plt.imshow(transformed_image.transpose())
    net.blobs['data'].data[...] = transformed_image
    #transformer.preprocess('data', caffe.io.load_image(imagePath))
                                                
    out = net.forward()
    # the output probability vector for the first image in the batch
    output_prob = out['prob'][0]   
    #print('predict label is: {}'.format(output_prob.argmax()))
    #break
    predict_class =output_prob.argmax()
    # record predict class
    predictResults[curLabel][predict_class] += 1
    # get top-5 predict class
    top_inds = output_prob.argsort()[::-1][:5]
    #print(top_inds)
    if curLabel in top_inds:
        top5 += 1
    #break
    #print('probabilities and labels:',zip(output_prob[top_inds],top_inds))
    # print('predict class is {0}, real class is {1}'.format(predict_class,name))
    curNums +=1
    if(curNums % 1000 == 0):
        print("already testing {0} files".format(curNums))
    if predict_class == curLabel:
        correctNums += 1
    else:
        fw.write('image is {0},'.format(imagePath))
        fw.write('predict class is {0}, real class is {1}.\n'.format(predict_class,curLabel))
        #break
        
    #break  
print('total nums are {0}, already finishing testing!'.format(totalNums))          
print('correct predict nums is {0}'.format(correctNums))
print('Top-1 accuracy is {0}'.format((correctNums * 1.0 / totalNums)))
print('Top-5 accuracy is {0}'.format((top5 * 1.0 / totalNums)))

fw.write("predict result:\n")
for key in predictResults.keys():
    # compute accuracy of every class
    right = int(predictResults[key][key])
    sums = sum(predictResults[key])
    accu = right*1.0/sums
    fw.write("current class is {0}, accuracy is {1}({2}/{3})\n".format(key,accu,right,sums))
    contents = str(predictResults[key]) + '\n'
    fw.writelines(contents)

fw.write("\nstatistic result:\n")
fw.write('total nums are {0}\n'.format(totalNums))          
fw.write('correct predict nums is {0}\n'.format(correctNums))
fw.write('top-1 accuracy is {0}, top-5 is {1}.\n'.format((correctNums * 1.0 / totalNums),(top5*1.0 / totalNums)))
fw.write('model path:{0}'.format(trainedModelPath))
fw.close()
end = time.time()
endTime = time.ctime()
print("start at %s\nend at %s" % (startTime, endTime))
print("total use %s seconds" % (end - start))



    
    
    
    
    
    
    

