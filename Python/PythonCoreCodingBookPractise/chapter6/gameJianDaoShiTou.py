#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 剪刀石头布的游戏

# 布：0， 石头：1， 剪刀：2
import random
dics = {
	'cloth': 0,
	'stone': 1,
	'scissor': 2
}

lists = ['cloth', 'stone', 'scissor']

while True:
	pr = 'Enter choice ' + ' '.join(lists) + ':(q to quit) '

	player = input(pr).strip().lower()
	if player not in dics.keys():
		print('please input the correct word!')
	if player == 'q':
		break

	computer = random.randint(0,2)
	print('player is %s ' % player)
	print('computer is %s ' % lists[computer])
	print('result: ')

	player = dics[player]
	if player == computer:
		print('no win')
	elif (computer > player and computer - player == 1):
		print('player win')
	else:
		print('computer win')

