# -*- coding: utf-8 -*-

'''
使用filter过滤非回数
'''

def is_palindrome(n):
	return n == int(str(n)[::-1])	#[::-1]倒序取序列中的元素

# Test
output = filter(is_palindrome, range(1, 1000))
print(list(output))