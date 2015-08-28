#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
some simplie math function
'''
import math

# 计算一元二次方程的解
def quadratic(a,b,c):
	delta = float(b **2 - 4 * a * c)
	# 如果delta > 0，则根据求根公式求解
	if delta > 0:
		x1 = float(-b + math.sqrt(delta)) / (2 * a)
		x2 = float(-b - math.sqrt(delta)) / (2 * a)
		return 'x1 = '+ str('%.2f'% x1) + ',x2 = ' + str('%.2f' % x2)
	elif delta == 0:
		x = float(-b / (2 * a))
		return 'x = ' + str('%.2f' % x)
	# 如果delta小于0，则两个解是复数
	else:
		delta *= -1
		re = -b / (2 * a)
		im = math.sqrt(delta)
		x1 = str('%.2f' % re) + "+" + str('%.2f' % im) + 'i'
		x2 = str('%.2f' % re) + "-" + str('%.2f' % im) + 'i'
		return 'x1 = ' + x1 + ',' + ' x2 = ' + x2
