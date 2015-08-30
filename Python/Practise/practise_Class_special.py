# -*- coding: utf-8 -*-

# 定制类
# 自定义__str__(),__repr__()
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name

	# __str__返回用户看到的字符串，使用print方法时输出的字符串
	def __str__(self):
		return 'Student object (name: %s)' % self.name

	# __repr__返回程序开发者看到的字符串，是直接在命令行输入类实例得到的字符串
	__repr__ = __str__

# __iter__方法
class Fib(object):
	'''
	实现斐波那契数列
	'''
	def __init__(self):
		self.a, self.b = 0, 1 	# 初始化两个计数器a， b

	def __iter__(self):
		return self 	# 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b	# 计算下一个值
		if self.a > 100000:	# 退出循环的条件
			raise StopIteration()
		return self.a # 返回下一个值

class Fibs(object):
	# __getitem__()方法可以实现像list按照下标取出元素
	def __getitem__(self, n):
		if isinstance(n, int):	# n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(self, slice):	  # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L


# Test
s = Student('John')
print(s)

for n in Fib():
	print(n)

f = Fibs()
print(f[:5])
print(f[:10])
print(f[0:6])