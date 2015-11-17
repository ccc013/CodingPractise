# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:12:36 2015

@author: cai
"""

from __future__ import print_function
from sklearn.datasets import load_svmlight_file
from sklearn import datasets
from sklearn.multiclass import OneVsOneClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
import sklearn.svm as svm
import numpy as np
from sklearn.externals import joblib
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression

import time,os

rootPath = '/home/cai/dataset/foodIngredients/'
featuresDirPath = rootPath + 'examples/_temp/total_features_libsvm/'
modelDirPath = featuresDirPath + 'svmModelsOneVsRest'
if not os.path.isdir(modelDirPath):
    os.mkdir(modelDirPath)
    print('make a dir{0}'.format(modelDirPath))

train_feature_path = featuresDirPath + 'train_features_fc7_libsvm.txt'
test_feature_path = featuresDirPath + 'val_features_fc7_libsvm.txt'
modelPath = featuresDirPath + 'svmModelsOneVsRest/svmTrainModel.pkl'

startTime = time.ctime()
start = time.time()


X_train, y_train = load_svmlight_file(train_feature_path)
X_test, y_test = load_svmlight_file(test_feature_path)


#X = np.array([[1,1], [2,2], [-1,2], [-2,3], [-1,-1], [-2,-3], [2,-4], [3,-5]])
#y = np.array([0, 0, 1, 1, 2, 2, 3, 3])
print('start at %s' % startTime)
print('start training...')
clf = OneVsOneClassifier(LinearSVC(random_state = 0))
#clf = OneVsRestClassifier(LinearSVC(random_state = 0))
clf = clf.fit(X_train, y_train)
print(clf.get_params())
#joblib.dump(clf, modelPath)   # save the trained model

#lists =[[5, -1], [-2, -6], [2,1], [-2, 5]] 
#test = np.array(lists)
#test_label = np.array([3, 2, 0, 1])
print("start predicting...")

#clf = joblib.load(modelPath)   # load the model
score = clf.score(X_test, y_test)
print('accuracy is {0}'.format(score))
#==============================================================================
# count = 0
# predictions = clf.predict(X_test)
# lens = len(predictions)
# for i in xrange(lens):
#     if predictions[i] == y_test[i]:
#         count +=1
# print('accuracy is %f' % (float(count) / lens ))
#==============================================================================

endTime = time.ctime()
end = time.time()
print("start at %s, end at %s" % (startTime, endTime))
print("consume ", (end - start))