# -*- coding: utf-8 -*-

from functools import reduce

# 利用reduce函数实现对list求积
def prod(L):
	return reduce(lambda x, y: x * y, L)

# 利用map和reduce编写一个str2floot函数，将字符串转换为浮点数
def str2floot(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

	def char2int(s):
		return reduce(lambda x, y: x * 10 + y, map(char2num, s))

	Ln = s.split('.')  # 将字符串根据.号分成整数部分和小数部分
	result = char2int(''.join(Ln)) # 通过join函数将整数和小数联合在一起生成一个整数
	return (result) / (10 ** len(Ln[1]))	


# Test
print('3 * 5 * 7 * 9 =',prod([3, 5, 7, 9]))
print('str2floot(\' 123.456 \') =', str2floot('123.456'))