# -*- coding: utf-8 -*-

# 装饰器的练习
import functools

def log(*text):
	def decorator(func):
		@functools.wraps(func) # 保持func的名字不变，该例子中就是func.__name__ = now1 （now2）
		def wrapper(*args, **kw):
			if len(text) == 0:
				print('call %s():' % func.__name__)
			else:
				print('%s %s():' % (text[0],func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log()  # 这里相当于 now1 = log(now1)
def now1():
	print('hello,python3')

@log('execute')  # 这里相当于 now2 = log('execute')(now2)
def now2():
	print('hello,python3')

# Test
now1()
now2()