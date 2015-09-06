# -*- coding: utf-8 -*-

# JSON

import json

# 序列化
d = dict(name='Bob', age=20, score=88)	# 创建一个字典
print(json.dumps(d))		# dumps()方法返回一个str，内容是标准的JSON

# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

# 序列化class
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

	# 转换方法，用于将class序列化成JSON
	def student2dict(std):
		return {
			'name': std.name,
			'age': std.age,
			'score': std.score
		}
		
s = Student('Bob', 23, 99)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)
print('Dump Student:', std_data)
# 反序列化
rebuild = json.loads(std_data, object_hook = lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)