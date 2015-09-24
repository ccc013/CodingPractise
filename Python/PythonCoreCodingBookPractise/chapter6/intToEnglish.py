#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# int(0 - 1000) convert to English

def intToEnglish(num):
	englishList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	num = int(num)

	if num < 10:
		return englishList[num]
	elif num < 100 :
		num_ten = num // 10
		num_single = num % 10
		return englishList[num_ten] + '-' + englishList[num_single]
	elif num < 1000 :
		num_hundred = num // 100
		num_ten = (num % 100) // 10
		num_1 = num % 10
		return englishList[num_hundred] + '-' + englishList[num_ten] + '-' + englishList[num_1]

# test
while True:
	num = input('Enter a num(q to quit): ')
	if num == 'q':
		break
	print(intToEnglish(num))
