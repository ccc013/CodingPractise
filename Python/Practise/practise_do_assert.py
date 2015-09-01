# -*- coding: utf-8 -*-

# use assert

def foo(s):
	n = int(s)
	assert n != 0, ' n is zero' # 断言,表达式n！=0应该是True，否则抛出AssertionError
	return 10 / n

def main():
	foo('0')

# Test
main()