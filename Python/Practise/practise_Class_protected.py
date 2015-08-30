#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程练习: 类和访问限制

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		# 属性名称前加上__使其变为私有变量，则只能内部访问，外部不能访问
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:  # 对参数score检查，score必须满足在0-100分，否则报错
			self.__score = score
		else:
			raise ValueError('bad score')

# Test
bart = Student('Bart Simpson', 98)
john = Student('John Snow', 99)
bart.print_score()
john.print_score()

