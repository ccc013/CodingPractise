#!usr/bin/env python3
# -*- coding: utf-8 -*-

# change upper to lower or lower to upper

def mySwapcase(strings):
	strs = []
	for i in strings:
		if i.isalpha():
			if i.isupper():
				i = i.lower()
			else:
				i = i.upper()
		strs.append(i)
	return ''.join(strs)

# test
if __name__ == '__main__':
	while True:
		testString = input('Enter a string(q to quit): ')
		if testString.strip().lower() == 'q':
			break
		print(mySwapcase(testString))