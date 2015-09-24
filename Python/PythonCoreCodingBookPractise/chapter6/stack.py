#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# simulate stack using list

stack = []

def pushit():
	stack.append(str(input(' Enter New string: ')).strip())

def popit():
	if len(stack) == 0:
		print('Cannot pop from an empty stack!')
	else:
		print('Removed [', stack.pop(), ']')

def viewstack():
	print(stack)     # calls str() internally

CMDs = {'u': pushit, 
		'o': popit,
		'v': viewstack}

def showmenu():
	pr = """
	p(U)sh
	p(O)p
	(V)iew
	(Q)uit

	Enter choice: """

	while True:
		while True:
			try:
				choice = str(input(pr).strip()[0].lower())
			except (EOFError, KeyboardInterrupt, IndexError):
				choice = 'q'

			print('\nYou picked: [%s]' % choice)
			if choice not in 'uovq':
				print('Invalid option, try again')
			else:
				break

		if choice == 'q':
			break
		CMDs[choice]()

if __name__ == '__main__':
	showmenu()
