# coding:utf-8
# 百度贴吧爬虫例子

import string,urllib2
import sys

#定义爬百度贴吧函数
def baidu_tieba(url,begin_page,end_page):
	for i in range(begin_page,end_page + 1):
		sName = string.zfill(i,5) + '.html'	# 自动填充成六位的文件名
		print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '...'
		with open(sName,'w+') as f:
			m = urllib2.urlopen(url + str(i)).read()
			f.write(m)


#输入参数
reload(sys)
sys.setdefaultencoding("utf-8")
bdurl = str(raw_input(u'请输入贴吧的地址，去掉pn=后面的数字：\n'))
begin_page = int(raw_input(u'请输入开始的页数: \n'))
end_page = int(raw_input(u'请输入终点的页数: \n'))

#调用函数
baidu_tieba(bdurl,begin_page,end_page)