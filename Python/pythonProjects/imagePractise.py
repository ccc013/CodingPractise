# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:29:30 2015

@author: cai
"""

import Image, time

rootPath = '/home/cai/dataset/food-101/'

trainTxtPath = rootPath + 'data/train_meta.txt'
valTxtPath = rootPath + 'data/val_meta.txt'

# vetifiy whether the imagePath is correct
def vetifyImagePath(path):
    with open(path) as fr:
        contents = fr.readlines()
        errorList =[]
        for index,content in enumerate(contents):
            # compute the time
            start = time.time()
            idx = content.index(' ')
            imageName = rootPath + content[:idx].strip()
            if not Image.open(imageName):
                print 'error path %s' % imageName
                errorList.append(imageName)
                #print 'ok!'
                #print im.size, im.format, im.mode
                #print imageName
            print 'finish %d' % index
        else:
            if len(errorList) != 0:
                print errorList
            else:
                print 'all the path is fine!'
            end = time.time()
            print "read: %f s" % (end - start)


# test
#vetifyImagePath(trainTxtPath)
vetifyImagePath(valTxtPath)

