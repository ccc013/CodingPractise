#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 爬取第九街市网站上食材的名称
import urllib, urllib2
import re
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


class foodInfoSpider(object):
	"""docstring for foodInfoSpider"""
	def __init__(self, baseUrl,rootCategory,flag):
		# base链接地址
		self.baseUrl = baseUrl
		# 标志，下载材料还是菜谱名
		self.flag = flag
		# 类别
		self.rootCategory = rootCategory
		# 保存的文件名
		self.file = None

		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		#初始化headers
		self.headers = {'User-Agent':self.user_agent}

	# 传入页码和菜系名字，获取该菜系首页的html内容
	def getPage(self,pageNum,rootCategory):
		try:
			# if pageNum == 1:
			# 	url = self.baseUrl + mealName + '/'
			# else:
			# 	url = self.baseUrl + mealName + '/list_' + str(pageNum) + '.htm' 
			if self.flag == 0:
				url = self.baseUrl + '.aspx?RootCategory=' + rootCategory + '&d9pageid=' + str(pageNum) ;
			elif self.flag == 1:
				url = self.baseUrl + '?d9pageid=' + str(pageNum)
			# print url
			request = urllib2.Request(url, headers = self.headers)
			response = urllib2.urlopen(request)
			
			return response.read()#.decode('gb2312')
		# 无法连接，报错
		except urllib2.URLError, e:
			if hasattr(e,"reason"):
				print u"连接失败，错误原因",e.reason
				return None
		
	# 获取该菜系页数和每页显示的菜谱数量
	def getPageNum(self, page):
		# pattern = re.compile('<div class="box".*?<div class="apage" style>(.*?)</div>',re.S)
		# result = re.search(pattern, page)
		soup = BeautifulSoup(page,"html.parser")
		result = soup.select('#ctl00_ContentPlaceHolder1_urlpage1_lblStatus')
		lists = str(result).split(' ')
		pageNum = ''
		for n in lists[-2]:
			if n is not '-':
				pageNum += str(n)
		return pageNum
		# for item in soup.find_all("div", class_="apage", limit = 1):

		# 	print unicode(item)
		# if result:
		# 	print unicode(result)
		# 	pageNum = result.group(1).strip()#.split('_')[1]
		# 	print pageNum
		# 	return pageNum
		# else:
		# 	return None

	# 获取食材名字
	def getContent(self, page):
		soup = BeautifulSoup(page,"html.parser")
		if self.flag == 0:
			pattern = re.compile('<div class="ti_ttnr01.*?<a href.*?>(.*?)</a>')
		elif self.flag == 1:
			pattern = re.compile('<div class="ti_ttnr".*?<a href.*?>(.*?)</a>')
		results = re.findall(pattern, page)
		contents = []
		for result in results:
			content = result.strip()
			# print unicode(content)
			contents.append(content)
		# print len(contents)
		if self.flag == 0:
			return contents[4:]
		else:
			return contents


	# 获取TXT文件名称
	def getFileName(self, page):
		pattern = re.compile('<head.*?<title>(.*?)</title>',re.S)
		result = re.search(pattern, page)
		if result:
			return result.group(1).strip()
		else:
			return None

	def setFileName(self, Title):
		if Title is not None:
			# print unicode(mealTitle)
			if self.flag == 0:
				titles = Title.split(',')
			elif self.flag == 1:
				titles = Title.split(' ')
			fileName = titles[0]
			# print unicode(fileName)
			self.file = open(unicode(fileName) + '.txt', 'w+')
		else:
			self.file = open('foodInfo.txt', 'w+')

	def writeData(self, contents):
		strs= [x for x in range(10)]
		strs = str(strs)
		strs += '('
		# 对食材的名字进行处理，去除不必要的信息	
		lens = len(contents)
		info = str(lens) + '\n'
		self.file.write(info)
		for item in contents:
			for idx, i in enumerate(item):
				if i in strs:
					item = item[0:idx]
					break
			# print unicode(item)
			item += '\n'
			self.file.write(item)#.encode('gb2312'))

		

	def start(self):
		# mealName = self.mealName
		rootCategory = self.rootCategory
		indexPage = self.getPage(1,rootCategory)
		print 'pageNum: '
		pageNum = self.getPageNum(indexPage)
		print pageNum
		#print 'pageNum = %s' % pageNum
		filename = self.getFileName(indexPage)
		self.setFileName(filename)
		if pageNum == None:
			print u"URL已失效，请重试"
			return 
		try:
			print u'共有' + pageNum + '页.'
			for i in range(1, int(pageNum) + 1):
				print u'正在读取第' + str(i) + '页'
				# if indexPage != 'None':
				# contents = self.getContent(indexPage)
				#print contents
				page = self.getPage(i, rootCategory)
				content = self.getContent(page)
				self.writeData(content)
				# else:
				# 	print 'error'
		except IOError, e:
			print u'写入异常，原因：', e.message
		finally:
			print u'写入完成！'
			#f.close()
			self.file.close()
		

# baseUrl = "http://www.d9js.com/ProductUI/ProductList"
# #mealName = ['yue',]
# rootCategory = ['0101','0102','0103']
# # 0 表示下载食材名字， 1 为菜谱名
# flag = 0 
# for category in rootCategory:
# 	print u'类别--' + str(category)
# 	spider = foodInfoSpider(baseUrl,category, flag)
# 	spider.start()

# 下载菜谱名
flag = 1
baseUrl = "http://www.d9js.com/ProductUI/FoodList.aspx"
spider = foodInfoSpider(baseUrl, '', flag)
spider.start()
