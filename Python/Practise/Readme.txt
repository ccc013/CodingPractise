在学习python3过程中练习的代码，包括有：
1.函数式编程：
（1）map函数：求积
（2）reduce函数：str2float函数将字符串转为浮点数，char2int函数将字符转为整型；
（3）filter函数：获取素数，过滤非回数；
（4）sorted函数；
（5）装饰器：practiseDecorator.py;
（6）偏函数：practisePartialFuntion.py

2.知识点的记录及练习：
（1）函数的参数

3.经典问题的解决：
（1）汉诺塔的实现：practiseHanluota.py;
 (2) 杨辉三角的实现：practiseTriangles.py

4.算法问题：
（1）快速排序算法:practiseQuickSort.py

5.模块简单使用例子:practiseModule1.py

6.面向对象编程：
（1）类和访问限制：practice_Class_protected.py
（2）继承和多态：practise_Class_animals.py
（3）使用__slots__限制类实例定义的属性：practise_use_slots.py
（4）使用@property:practise_use_property.py,practise_use_property2.py
（5）使用定制类:自定义一些特殊的方法，如__str__,__iter__等，practise_Class_special.py
（6）使用枚举类:practise_use_enum.py

7.错误、调试和测试
（1）错误处理:practise_do_try.py,practise_err_logging.py,practise_err_raise.py
（2）调试:print方法,assert->practise_do_assert.py, logging->,practise_do_logging.py
		  pdb方法，在命令行中使用python3 -m pdb file 可以启动pdb调试器->practise_use_pdb.py
（3）单元测试:可以在命令行使用python3 -m unittest filename直接运行单元测试，这样可以批量测试；
			  或者如mydict_test.py中添加最后两行代码。
（4）文档测试：mydict2.py,fact_doctest.py
8.IO编程
（1）StringIO和BytesIO：do_stringIO.py,do_bytesIO.py
（2）利用os模块实现在当前目录及其所有子目录下查找文件名包含特定字符串的文件：practise_select_filename.py
（3）序列化：把变量从内存中变成可存储或传输的过程称之为序列化:
			 Python中提供了pickle模块来实现。但pickle只适用于Python-->use_pickle.py
			 JSON:use_json.py
9.进程和线程
（1）多进程：multi_processing.py,
	使用Pool批量创建子进程：pool_processing.py,
	使用subprocess模块创建子进程：do_subprocess.py
	进程间的通信：do_queue.py
（2）线程：
