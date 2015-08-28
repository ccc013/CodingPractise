# -*- coding: utf-8 -*-

'''
实现杨辉三角
'''
# n表示输出的行数
def triangles(n):
	L = [1]
	i = 0	# 计数
	while i < n:
		yield(L)	# 生成器
		L.append(0)
		L = [ L[j] + L[j - 1] for j in range(len(L))]
		i += 1
	return

# Test:输出10行
g = triangles(10)
for i in g:
	print(i)