#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findchr(string, char):
	'''
	find the char in string,if can find, return index,or return -1
	'''
	if char not in string:
		return -1
	for idx, val in enumerate(string):
		if val == char:
			return idx

def rfindchr(string, char):
	'''
	find the char last in string
	'''
	if char not in string:
		return -1
	lens = len(string)
	for i in range(-1, -lens, -1):
		if string[i] == char:
			return (lens + i)

def subchr(string, origchar, newchar):
	'''
	If find the char in the string, then use newchar to replace origchar and return the new string
	'''
	if origchar not in string:
		return -1
	lens = len(string)
	# change to list because list can change
	slist = list(string)
	
	for i in range(0, lens):
		if slist[i] == origchar:
			slist[i] = newchar
	return ''.join(slist)

if __name__ == '__main__':
	# test
	#print(findchr('python', 'y')) # Prints 1
	#print(findchr('hello', 'a'))  # Prints -1

	#print(rfindchr('hello', 'l'))
	#print(rfindchr('acdeadcaegac', 'e'))

	print(subchr('hello','l','n'))	# Prints henno
	print(subchr('python', 'n','py')) # Prints pythopy
	print(subchr('abcnda','a','q'))   # Prints qbcndq


