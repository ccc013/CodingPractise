# -*- coding: utf-8 -*-

# 使用Enum

from enum import Enum, unique

# 使用Enum的第一种方法，可以精确控制枚举类型
@unique
class Weekday(Enum):
	Sun = 0  # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

# Test
day1 = Weekday.Mon
print('day1 =', day1)								# Prints "day1 = Week.Mon"
print('Weekday.Tue =', Weekday.Tue)					# Prints "Weekday.Tue = Weekday.Tue"
print('Weekday[\'Tue\'] =', Weekday['Tue'])	    	# Prints "Weekday['Tue'] = Weekday.Tue"
print('Weekday.Tue.value =', Weekday.Tue.value) 	# Prints "Weekday.Tue.value = 2"
print('day1 == Weekday.Mon ?', day1 == Weekday.Mon)	# Prints "day1 == Weekday.Mon ? True"
print('day1 == Weekday.Tue ?', day1 == Weekday.Tue) # Prints "day1 == Weekday.Tue ? False"
print('day1 == Weekday(1) ?', day1 == Weekday(1))	# Prints "day1 == Weekday(1) ? True"

for name, member in Weekday.__members__.items():
	print(name, '=>', member)      	# Prints "Sun => Weekday.Sun
								   	#   	  Mon => Weekday.Mon
								   	#   	  Tue => Weekday.Tue
									#		  Wed => Weekday.Wed
									#		  Thu => Weekday.Thu
									#		  Fri => Weekday.Fri
									#		  Sat => Weekday.Sat"


# 使用枚举类的第二种方法
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)	# Prints "Jan => Month.Jan , 1
													#		  Feb => Month.Feb , 2
													#		  Mar => Month.Mar , 3
													#		  Apr => Month.Apr , 4
													#		  May => Month.May , 5
													#		  Jun => Month.Jun , 6
													#		  Jul => Month.Jul , 7
													#		  Aug => Month.Aug , 8
													#		  Sep => Month.Sep , 9
													#		  Oct => Month.Oct , 10
													#		  Nov => Month.Nov , 11
													#		  Dec => Month.Dec , 12

print(type(Enum))		# Prints "<class 'enum.EnumMeta'>"			
print(type(Month))		# Prints "<class 'enum.EnumMeta'>"
print(isinstance(Month.Jan, Month))	# Prints "True"
print(isinstance(Month.Jan, Enum))  # Prints "True"
print(isinstance(Enum, Month))		# Prints "False"
print(isinstance(Month, Enum))		# Prints "False"