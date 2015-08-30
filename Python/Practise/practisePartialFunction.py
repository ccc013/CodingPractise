# -*- coding: utf-8 -*-

# 偏函数的练习
import functools

int2 = functools.partial(int, base = 2)
print(int2('1000000'))