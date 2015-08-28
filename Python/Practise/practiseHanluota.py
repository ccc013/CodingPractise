# -*- coding: utf-8 -*-

'''
汉诺塔的移动，利用递归函数实现。
'''

def move(n, a, b, c):
	'''
	n表示3个柱子中A的盘子数量，a, b, c分别表示A、B、C三个柱子
	'''
	if n == 1:
	# 如果只有一个盘子，直接移动到C上面；
		print('move', a, '-->', c)
		return
	else:
	# 将A上面n-1个盘子利用C移到B：
		move(n-1, a, c, b)
	# 将A最下面的1个盘子移到C：
		move(1, a, b, c)
	# 将B中的n-1个盘子利用A移到C上面
		move(n-1, b, a, c)
		return

# Test
move(3, 'A', 'B', 'C')   # Prints:
						 # move A --> C
						 # move A --> B
						 # move C --> B
						 # move A --> C
						 # move B --> A
						 # move B --> C
						 # move A --> C