#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
练习：关于函数的参数
'''

# 默认参数,age 和 city 就是默认参数，而name，gender则是位置参数，也是必选参数
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name:', name,'gender:', gender,'age:', age,'city:', city)
	

# Test
enroll('Jack', 'B')  			 # Prints "name: Jack gender: B age: 6 city: Beijing"
enroll('Tom', 'A',age = 25)		 # Prints "name: Tom gender: A age: 25 city: Beijing"

# 可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum

# Test
print(calc(1,2,3))	# Prints "14"
nums = [1,2,3]
# Python 允许在list或tuple前添加*，把list或tuple的元素变成可变参数传进去
print(calc(*nums))	# Prints "14"


# 关键字参数,关键字参数kw
def person(name, age, **kw):
	print('name:', name, 'age:', age,'other:',kw)

# Test
person('Bob', 35)	# Prints "name: Bob age: 35 other: {}"
person('Adam', 25, city = 'Beijing')	# Prints "name: Adam age: 25 other: {'city': 'Beijing'}"
extra = {'city': 'Beijing', 'job': 'Engineer'}
# 可以在dict前加**将dictionary中的元素传入函数的**kw中 
# 作为关键字参数的dict中的key值必须是string
person('Jack', 24 , **extra)	# Prints "name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}"

# 命名关键字参数，可以限制关键字参数的名字
def person1(name, age, *, city, job):
	print(name, age, city, job)

# Test
# 命名关键字参数必须传入参数名，否则会视为位置参数
person1('Jack', 24, city ='Beijing', job='Engineer') # Prints "Jack 24 Beijing Engineer"