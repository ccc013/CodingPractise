#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'ccc'

import sys

def test():
	args = sys.argv  # argv变量是用list存储了命令行的所有参数，至少有一个参数，即该.py文件的名字
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__ == '__main__':	# 只有在命令行运行该文件才执行，否则导入则不会执行test()
	test()