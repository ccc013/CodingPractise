# coding:utf8
# 使用Debug Log

import urllib2

httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler,httpsHandler)
urllib2.install_opener(opener)
url = 'http://www.baidu.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()