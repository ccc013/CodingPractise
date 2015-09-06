# -*- coding: utf-8 -*-

# 在当前目录及其所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径

import os

def select(filename, path = '.'):
	_list = [x for x in os.listdir(path)]
	for _file in _list:
		if os.path.isfile(os.path.join(path,_file)):
			if filename in _file:
				print(_file, u'相对路径', path)
		elif os.path.isdir(os.path.join(path,_file)):
			select(filename, os.path.join(path,_file))

# Test
print(select('prac'))
