# -*- coding: utf-8 -*-

# 错误处理，使用try..except..finally
# 输出一个除法运算错误：
# try...
# except: division by zero
# finally...
# END
try:
	print('try...')
	r = 10 / 0			
	print('result:', r)
except ZeroDivisionError as e:
	print('except:', e)
finally:
	print('finally...')
print('END')


# 输出一个ValueError：
# try...
# ValueError: invalid literal for int() with base 10: 'a'
# finally...
# END
try:
	print('try...')
	r = 10 / int('a')	# int()函数可能会抛出ValueError		
	print('result:', r)
except ValueError as e:	# except不仅捕获该类型的错误，还会捕获其子类
	print('ValueError:', e)
except ZeroDivisionError as e:
	print('except:', e)
else:	# 没有错误发生，执行else语句
	print('no error!')
finally:
	print('finally...')
print('END')