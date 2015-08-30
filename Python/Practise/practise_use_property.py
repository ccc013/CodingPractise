# coding: utf-8 -*-

# 使用@property

class Student(object):
	"""docstring for Student"""

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0-100!')
		self._score = value

	@property
	def birth(self):
	    return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
	    return 2015 - self._birth
	

# Test
s = Student()
s.set_score(60) 
print(s.get_score()) # Prints '60'
try:
	s.set_score(150)
except ValueError as e:
	print('ValueError:', e)

s.birth = 1992  # 相当于s.set_birth(1992)
print(s.birth)  # 相当于s.get_birth()
print(s.age)