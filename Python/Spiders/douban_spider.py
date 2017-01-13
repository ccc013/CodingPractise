#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/1/13 21:36
@Author  : cai

用于抓取豆瓣电影的爬虫
"""
import string
import re
import urllib.request as url_request
import urllib.error as url_error

class DoubanSpider(object):
    """
    本类主要用于抓取豆瓣电影Top 100的电影名称

    Attributes:
        page: 用于表示当前所处的抓取页面
        cur_url：用于表示当前争取抓取页面的url
        datas：存储处理好的抓取到的电影名称
        _top_num：用于记录当前的top号码
    """

    def __init__(self):
        self.page = 1
        self.cur_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
        print("豆瓣电影爬虫准备就绪，准备爬取数据...")

    def get_page(self, cur_page):
        """
        根据当前页码爬取网页HTML
        :param cur_page:
        :return:
            返回抓取到整个页面的HTML

        """
        url = self.cur_url
        try:
            my_page = url_request.urlopen(url.format(page = (cur_page -1) * 25)).read().decode("utf-8")
        except url_error.URLError as e:
            if hasattr(e, "code"):
                print("The server couldn't fulfill the request.")
                print("Error code: %s", e.code)
            elif hasattr(e, "reason"):
                print("We failed to reach a server. Please check your url and read the Reason")
                print("Reason: %s", e.reason)
        return my_page

    def find_title(self, my_page):
        """
        通过返回的整个网页HTML, 正则匹配前100的电影名称
        :param my_page:
        :return:
        """
        temp_data = []
        move_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
        #print(move_items)
        for index, item in enumerate(move_items):
            if item.find("&nbsp") == -1:
                temp_data.append("Top" + str(self._top_num) + " " + item)
                self._top_num += 1
        self.datas.extend(temp_data)

    def start_spider(self):
        """
        爬虫入口，并控制爬虫抓取页面的范围
        :return:
        """
        while self.page <= 4:
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1

def main():
    print("""
        ###############################
            一个简单的豆瓣电影前100爬虫
            Author: cai
            Version: 0.0.1
            Date: 2017-01-13
        ###############################
    """)
    my_spider = DoubanSpider()
    my_spider.start_spider()
    for item in my_spider.datas:
        print(item)
    print("豆瓣爬虫爬取结束...")

if __name__ == '__main__':
    main()