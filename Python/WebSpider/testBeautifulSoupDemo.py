# coding:utf-8
# 练习使用beautifulsoup库

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)
print soup.prettify()  #格式化输出
print soup.title	   #查找到第一个标签为title并输出
print soup.a           
print soup.p
# Tag 有name和attrs两个属性
print soup.name
print soup.head.name
print soup.p.attrs
#获取标签内部的文字内容可以使用string方法
print soup.p.string
print type(soup.p.string)	#它的类型是NavigableString
