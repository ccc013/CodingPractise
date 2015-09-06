# -*- coding: utf-8 -*-

# StringIO，即在内存中读写str
from io import StringIO

# 把str写入StringIO
f = StringIO()	# 创建一个StringIO对象
f.write('hello world!')		
print(f.getvalue())		

# 读取StringIO
fr = StringIO('Hello!\nPython\n321')
while 1:
	s = fr.readline()
	if s == '':
		break
	print(s.strip())
