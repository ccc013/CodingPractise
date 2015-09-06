# -*- coding: utf-8 -*-

import pickle

# 把一个对象序列化后写入文件
d = dict(name='Bob', age=20, score=88)	# 创建一个字典
pickle.dumps(d)		# pickle.dumps()方法把任意对象序列化成一个bytes

# 使用pickle.dump()方法可以直接把对象序列化后写入文件
with open('dump.txt', 'wb') as f:
	pickle.dump(d, f)

# 从磁盘中读取到内存中
fr = open('dump.txt', 'rb')
d = pickle.load(fr)
fr.close()
print(d)
