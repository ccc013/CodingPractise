# coding: utf-8 -*-

# 使用__slots__变量来限制类实例可以添加的属性

class Student(object):
	"""docstring for Student"""
	__slots__ = ('name', 'age')	# 用tuple定义允许绑定的属性名称

class GraduateStudent(Student):
	pass
		
class HighStudent(Student):
	"""docstring for HighStudent"""
	__slots__ = ('score')
		

# Test
s = Student() # 创建新的实例
s.name = 'John' # 绑定属性‘name’
s.age = '25'	# 绑定属性‘age’
try:
	s.score = 78	# 绑定属性‘score’
except AttributeError as e:
	print('AttributeError:', e)

# __slots__并不限制类属性的添加
Student.city = 'Beijing'
print(Student.city)
print(s.city)

gs = GraduateStudent()
gs.age = 25
gs.score = 99  # __slots__定义的属性仅对当前类实例起作用，对继承的子类不起作用
print(gs.score)

hs = HighStudent()
hs.name = 'Tom'
hs.age = 17
hs.score = 88
# 子类中也定义了__slots__，则其实例允许定义的属性就是自身和父类的__slots___
try:
	hs.weight = 100	# 绑定属性‘weight’
except AttributeError as e:
	print('AttributeError:', e)

		