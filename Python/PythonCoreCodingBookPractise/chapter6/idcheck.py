#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 标识符合法性检查，首先要以字母或者下划线开始，后面要跟字母、下划线或者数字。

import string,keyword

alphas = string.ascii_letters + '_'
nums = string.digits

print ('Welcome to the Identifier Checker v1.0')
print ('Testees must be at least 2 chars long.')

while True:
	myInput = input('Identifier to test?(q to quit) ')

	if myInput.strip().lower() == 'q':
		print('quit')
		break

	length = len(myInput)
	if length == 1:
		
		if myInput[0] not in alphas:
			print('invalid: symbol must be alphabetic')
		else:
			print('okay as an identifier')

	elif length > 1:

		if myInput[0] not in alphas: 
			print ('''invalid: first symbol must be alphabetic''')
		elif myInput[:] in keyword.kwlist:
			print('invalid: cannot use keyword')
		else:
			for otherChar in myInput[1:]:
				alphnums = alphas + nums
				if otherChar not in alphnums:
					print ('''invalid: remaining symbols must be alphabetic''')
					break
			else:
				print ("okay as an identifier")