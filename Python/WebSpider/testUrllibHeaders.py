# coding:utf8
# 该例子仅仅用于说明如何设置headers

import urllib
import urllib2

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc','password':'XXXX'}
headers = {'User-Agent':user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
page = response.read()
