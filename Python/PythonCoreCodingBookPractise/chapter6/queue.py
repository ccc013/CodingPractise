#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# simulate queue using list

queue = []

def enQ():
	queue.append(str(input(' Enter New string: ').strip()))

def deQ():
	if len(queue) == 0:
		print('Cannot pop from an empty queue!')
	else:
		print('Removed [', queue.pop(0), ']')

def viewQ():
	print(queue)

CMDs = {'e': enQ,
		'd': deQ,
		'v': viewQ}

def showmenu():
	pr = """
	(E)nqueue
	(D)equeue
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
			if choice not in 'devq':
				print('Invalid option, try again')
			else:
				break

		if choice == 'q':
			break
		CMDs[choice]()

if __name__ == '__main__':
	showmenu()
