# -*- coding: utf-8 -*-

# 使用@property练习

class Screen(object):
	"""docstring for Screen"""
	
	@property
	def width(self):
	    return self._width
	
	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
	    return self._height
	
	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
	    return self.width * self.height

# Test
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
# 假设结果为786432，如果不是则会报错
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
	
		