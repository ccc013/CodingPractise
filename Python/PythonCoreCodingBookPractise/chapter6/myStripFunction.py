#!usr/bin/env python3
# -*- coding: utf-8 -*-

# create a funciton which can work as string.strip()

def myStripFunction(strings):
	length = len(strings)
	print('You input: %s, length = %d.' % (strings, length))
	start = 0
	end = 0
	for i in range(0, length):
		if not strings[i].isspace():
			start = i
			break
	for i in range(-1,-length, -1):
		if not strings[i].isspace():
			end = length + i + 1
			break
	return len(strings[start:end]), strings[start:end]

# test
while True:
	testString = input(' Enter a string(q to quit): ')
	if testString.strip().lower() == 'q':
		break
	print(myStripFunction(testString))