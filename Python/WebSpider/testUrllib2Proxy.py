# coding:utf8
# 本例子说明了代理的设置用法，urllib2默认会使用http_proxy来设置HTTP Proxy

import urllib2

enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)