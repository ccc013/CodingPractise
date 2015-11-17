# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:13:45 2015

@author: cai

"""

import urllib
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import socket

class Crawler(object):
    
    def __init__(self):
        # url to crawl
        self.url = 'http://image.baidu.com/' 
        # xpath of img element
        self.img_xpath = '//ul/li/div/a/img' 
        # xpath of img desc
        self.img_desc_xpath = '//ul/li[@class="imgitem"]'
        # xpath of downloadlink element
        # self.download_xpath = '//ul/li/div/div/a[@class="down"]'
        self.img_url_dic = {}
        # set the max images per class to downloads
        self.maxImages = 10
        # set file path
        self.rootPath = '/home/cai/dataset/'
        self.imageFilePath = self.rootPath + 'foodIngredients/web_testImages/'
        self.filePath = self.rootPath + 'test/'
        self.txtFile = self.rootPath + 'foodIngredients/images/classes.txt'
        self.logFile = self.rootPath + 'imageMessage.txt'
        self.flog = open(self.logFile, 'w')  
        # classes
        self.classes = 0
        
    # from txtFile get the name that will be used to search
    def getSearchNames(self):
        txtFile = self.txtFile
        names = []
        with open(txtFile) as fr:
            names = fr.readlines()
        return names
    
    # download images
    def downloads(self, driver, name):
        maxImgs = self.maxImages
        img_url_dic = self.img_url_dic
        img_desc_xpath = self.img_desc_xpath
        flog = self.flog
        
        # set timeout 
        socket.setdefaulttimeout(30)
        
        pos = 0
        i = 0
        count = 0
        print 'Downloading', unicode(name)
        while (count < maxImgs):
            # 模拟滚动窗口以浏览下载更多图片
            pos += i * 500
            
            # 每隔10页需要点击加载更多图片
            if i > 0 and i % 10 == 0:
                driver.find_element_by_id('pageMore').click()
            i += 1
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
           
            for img_desc_element in driver.find_elements_by_xpath(img_desc_xpath):
                img_url = img_desc_element.get_attribute('data-objurl')
                img_desc = img_desc_element.get_attribute('data-title')
                img_desc = self.filter_filename_str(img_desc)
                
                if img_url != None and not img_url_dic.has_key(img_url):
                    img_url_dic[img_url] = ''
                    ext = img_url.split('.')[-1]
                    imagePath = self.imageFilePath + \
                                str(self.classes) + '_' + str(count) + '.' + ext
                    # 判断图片是否已经存在
                    if os.path.isfile(imagePath):
                        count += 1
                        continue
                    
                    try:
                         #urllib.urlretrieve(img_url, imagePath)
                        urlopen = urllib.URLopener()
                        # 下载图片
                        fp = urlopen.open(img_url)
                        data = fp.read()
                        # 清除并以二进制写入
                        imageFile = open(imagePath, 'wb')
                        imageFile.write(data)
                        imageFile.close()
                        
                        sizes = os.path.getsize(imagePath)
                        flog.writelines("%s %s %s\n" % (imagePath, str(sizes), img_url))
                        # 统计成功下载图片的数量
                        count += 1
                        time.sleep(1)
                        print 'class ' + str(self.classes) + ', finish ' + str(count)
                    except IOError, e:
                        flog.writelines("%s %s %s\n" % (imagePath,e,img_url))
                        print "Fail download %s ... Error %s" % ( img_url,e)
                        
                if count >= maxImgs:
                    break
        return count

    def launch(self):
        # launch driver
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(self.url)
        assert '百度图片' in driver.title

        searchNames = self.getSearchNames()
        lens = len(searchNames)
        results = {}
        # 判断保存的目录是否存在
        if not os.path.isdir(self.imageFilePath):
            os.mkdir(self.imageFilePath)        
        
        for idx in range(lens):
            elem = driver.find_element_by_name('word')
            name = searchNames[idx].strip()
            searchContent = unicode(name)
            elem.send_keys(searchContent)
            elem.send_keys(Keys.RETURN)
            #assert unicode(name) in driver.title
            
            # start to download the image
            self.classes = idx
            downloadImgs = self.downloads(driver, name)
            info = unicode(name) + ' has downloads ' + str(downloadImgs) + ' images.'
            print info
            results[name] = downloadImgs
            self.classes += 1
            # clear the content of the search box
            elem = driver.find_element_by_name('word')
            elem.clear()
        
        print 'Done!'
        driver.close()
        
        # print the final result
        totalImgs = 0
        for key, value in results.items():
            print key + ': ' + str(value)
            totalImgs += value
        print 'There are ' + str(self.classes) + ' classes' + \
                ', total Images are ' + str(totalImgs)
    
    # filter invalid characters in filename
    def filter_filename_str(self, s):
        invalid_set = ('\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ')
        for i in invalid_set:
            s = s.replace(i, '_')
        return s
        
if __name__ == '__main__':
    crawler = Crawler()
    crawler.launch() 

