# coding:utf8
# 使用urllib和urllib2库，并使用Get方式传送，运行程序后返回登陆后呈现的页面内容

import urllib
import urllib2

values = {
		"username":"1016903103@qq.com",
		"password":"XXXX"
}
data = urllib.urlencode(values)  #使用urllib的urlencode方法将字典编码
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl