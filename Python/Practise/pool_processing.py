# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

# 启动大量的字进程，可以用进程池的方式批量创建子进程
def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)		# 设置Pool的大小，即最多同时执行进程数，Pool的默认大小是CPU的核数
	for i in range(5):
		p.apply_async(long_time_task, args =(i,))
	print('Waiting for all subprocesss done...')
	p.close()
	p.join()
	print('All subprocesss done...')
