在学习python3过程中练习的代码，包括有：
1. 函数式编程：

* map函数：求积
* reduce函数：str2float函数将字符串转为浮点数，char2int函数将字符转为整型；
* filter函数：获取素数，过滤非回数；
* sorted函数；
* 装饰器：practiseDecorator.py;
* 偏函数：practisePartialFuntion.py

2. 知识点的记录及练习：函数的参数

3. 经典问题的解决：
* 汉诺塔的实现：practiseHanluota.py;
* 杨辉三角的实现：practiseTriangles.py

4. 算法问题：
* 快速排序算法:practiseQuickSort.py

5. 模块简单使用例子:practiseModule1.py

6. 面向对象编程：

* 类和访问限制：practice_Class_protected.py
* 继承和多态：practise_Class_animals.py
* 使用__slots__限制类实例定义的属性：practise_use_slots.py
* 使用@property:practise_use_property.py,practise_use_property2.py
* 使用定制类:自定义一些特殊的方法，如__str__,__iter__等，practise_Class_special.py
* 使用枚举类:practise_use_enum.py

7. 错误、调试和测试
* 错误处理:practise_do_try.py,practise_err_logging.py,practise_err_raise.py
* 调试:
  **print方法**,assert->practise_do_assert.py, logging->,practise_do_logging.py
  **pdb方法**，在命令行中使用python3 -m pdb file 可以启动pdb调试器practise_use_pdb.py
* 单元测试:可以在命令行使用python3 -m unittest filename直接运行单元测试，这样可以批量测试；
   		  或者如mydict_test.py中添加最后两行代码。
* 文档测试：mydict2.py,fact_doctest.py
8. IO编程

* StringIO和BytesIO：do_stringIO.py,do_bytesIO.py
* 利用os模块实现在当前目录及其所有子目录下查找文件名包含特定字符串的文件：practise_select_filename.py
* 序列化：把变量从内存中变成可存储或传输的过程称之为序列化:
  Python中提供了pickle模块来实现。但pickle只适用于Python-->use_pickle.py
  JSON:use_json.py

9. 进程和线程

* 多进程：multi_processing.py,
   使用Pool批量创建子进程：pool_processing.py,
   使用subprocess模块创建子进程：do_subprocess.py
   进程间的通信：do_queue.py

* 线程：Python的标准库提供了两个模块：**_thread和 threading**，**_thread**是低级模块，**threading**是高级模块，对**_thread**进行了封装。绝大多数情况下，只需要使用**threading**这个高级模块。

* 任何进程默认会启动一个线程，该线程称之为主线程，主线程又可以启动新的线程，**threading**模块有个**current_thread()**函数，它可以永远返回当前线程的实例，主线程实例的名字叫**MainThread**。

   multi_threading.py

* 多线程和多进程最大的不同在于，**多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响；**而**多线程中，所以变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量。**

* 可以采用**Lock**的方法确保某段关键代码只能由一个线程从头到尾完整地执行，其坏处是，首先**阻止了多线程并发执行**，包含锁的某段代码实际上只能以单线程模式执行，效率大大下降；其次是由于可以存在多个锁，不同的线程持有不同的锁，在试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，即不能执行，也无法结束，只能靠操作系统强制终止。---do_Lock.py
