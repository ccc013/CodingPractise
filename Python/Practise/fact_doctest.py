# -*- coding: utf-8 -*-

def fact(n):
	'''
	Return the factorial of an integer, with number of other type it can raise corresponding error

	>>> fact(5)
	120

	>>> fact('abc')
	Traceback (most recent call last):
	...
	TypeError: unorderable types: str() < int()

	>>> fact(0)
	Traceback (most recent call last):
	...
	ValueError
	'''
	
	if n < 1 :
		raise ValueError()
	if n == 1:
		return 1
	return n * fact(n - 1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()