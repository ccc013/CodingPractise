# -*- coding: utf-8 -*-

# unittest

import unittest

from my_dict import Dict

class TestDict(unittest.TestCase):
	
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(d, dict)

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')
		
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty

	# 每个测试方法调用前后会打印setUp和tearDown方法
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')

# Test
if __name__ == '__main__':
	unittest.main()