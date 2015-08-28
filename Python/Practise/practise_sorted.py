# -*- coding: utf-8 -*-

# 使用sorted函数排序
def by_name(t):
	return t[0].lower()

def by_score(t):
	return t[1]
	

# Test
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key = by_name) # 按名字排序
L3 = sorted(L, key = by_score, reverse = True) # 按成绩从高到低排序
print(L2)
print(L3)