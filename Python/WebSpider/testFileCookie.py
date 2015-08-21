# coding:utf8
# 获取Cookie并保存到文件

import urllib2
import cookielib

filename = 'cookie.txt'	#设置保存cookie的文件
cookie = cookielib.MozillaCookieJar(filename)	#声明一个MozillaCookieJar对象实例来保存cookie,之后写入文件
handler = urllib2.HTTPCookieProcessor(cookie) #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(handler)	#通过handler来创建opener
response = opener.open('http://www.baidu.com')	#此处的open方法同urllib2的urlopen方法，也可以传入request
''' save方法中，第一个参数表示即使cookies将被丢弃也将它保存下来；
	第二个参数表示在该文件中如果cookie已经存在，则覆盖原文件写入
'''
cookie.save(ignore_discard = True, ignore_expires = True)

'''
从文件获取cookie并访问

cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard = True, ignore_expires = True)
req = urllib2.Request("http://www.baidu.com")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
'''