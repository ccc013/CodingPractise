# -*- coding: utf8 -*-

# 问题：有一个字符串，每次循环都把位于最后的一个字符砍掉，但第一次要显示所有字符串
# 实现小技巧：可以使用None作为索引值

s = "abcde"
for i in [None] + range(-1, -len(s), -1):
	print s[:i]