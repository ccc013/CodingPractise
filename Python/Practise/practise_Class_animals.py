#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程练习:继承和多态

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print(' Animal is running...')

class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print(' Dog is running..')

	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print(' Cat is running...')
# 定义一个有run方法但不是继承Animal
class Timer(object):
	def run(self):
		print(' Start...')

# 多态，只需要传入的对象有run方法即可
def run_twice(objHasRun):
	objHasRun.run()
	objHasRun.run()

# Test
dog = Dog()
dog.run()

cat = Cat()
cat.run()
		
run_twice(Animal())		
run_twice(Dog())
run_twice(Cat())
run_twice(Timer())