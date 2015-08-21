# coding:utf8
# 本例子展示了对URLError异常处理

import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
	urllib2.urlopen(req)
except urllib2.URLError, e:
	if hasattr(e,"code"):  # 捕获到HTTPError，则输出code，不会再处理URLError异常
		print e.code
	if hasattr(e,"reason"): # 发生的不是HTTPError，则再去捕获URLError，输出错误原因
		print e.reason	
else:
	print "OK"