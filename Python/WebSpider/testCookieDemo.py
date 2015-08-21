# coding:utf8
# 获取Cookie保存到变量

import urllib2
import cookielib

cookie = cookielib.CookieJar()	#声明一个CookieJar对象实例来保存Cookie
handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler)	#通过handler来创建opener
response = opener.open('http://www.baidu.com')	#此处的open方法同urllib2的urlopen方法，也可以传入request
for item in cookie: 
	print 'Name = ' + item.name
	print 'Value = ' + item.value