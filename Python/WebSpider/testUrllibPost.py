# coding:utf8
# 使用urllib和urllib2库，并使用Post方式传送,运行程序后返回登陆后呈现的页面内容

import urllib
import urllib2

values = {
		"username":"1016903103@qq.com",
		"password":"XXXX"
}
'''
这里字典的定义也可以如下：
values={}
values["username"] = "1016903103@qq.com"
values["password"] = "XXXX"
'''
data = urllib.urlencode(values)  #使用urllib的urlencode方法将字典编码
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()
