# coding:utf8
# 使用urllib2模块
import urllib2

request = urllib2.Request("http://www.baidu.com") 
response = urllib2.urlopen(request)				# urlopen参数可以传入一个request请求
print response.read()