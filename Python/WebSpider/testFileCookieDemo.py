# coding:utf8
# 利用cookie实现模拟登陆，并将cookie信息保存到文本文件

import urllib
import urllib2
import cookielib

filename = 'cookieTest.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			 'stuid':'201130302358',
			 'pwd':'21322587'
	})
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
try:
	result = opener.open(loginUrl,postdata)
except URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason

cookie.save(ignore_discard = True, ignore_expires = True)
# 利用cookie请求访问另一个网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
result = opener.open(gradeUrl)
print result.read()

