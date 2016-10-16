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
from selenium.common.exceptions import ElementNotVisibleException,StaleElementReferenceException
import socket

class Crawler(object):
    
    def __init__(self):
        # url to crawl
        self.url = 'http://image.baidu.com/' 
        # xpath of img element
        self.img_xpath = '//ul/li/div/a/img' 
        # xpath of img desc
        self.img_desc_xpath = '//ul/li[@class="imgitem"]'
        self.img_url_dic = {}
        # set the max images per class to downloads
        self.maxImages = 10
        # 根目录
        self.rootPath = 'D:\\图片\\test'
        # 保存图片的文件夹路径
        self.imageFilePath = os.path.join(self.rootPath,'image')
       # self.filePath = self.rootPath + 'test/'
        # 保存要下载的图片的类的文本文件
        self.txtFile = os.path.join(self.rootPath,'classes.txt')
        # 搜索的关键词
        self.searchNameTxtFile = os.path.join(self.rootPath,'classes.txt')
        # 日志文件
        self.logFile = os.path.join(self.rootPath,'log.txt')
        self.flog = open(self.logFile, 'w')  
        # classes
        self.classes = 0
        
    # from txtFile get the name that will be used to search
    def getSearchNames(self):
        txtFile = self.searchNameTxtFile
        names = []
        with open(txtFile) as fr:
            names = fr.readlines()
        return names
    
    # 创建类文件夹并返回文件夹路径
    def create_folder(self,name):
        imageDir = os.path.join(self.imageFilePath,name.strip())
        if not os.path.isdir(imageDir):
            os.mkdir(imageDir)  
        return imageDir
    
    # download images
    # name: 图片类名字；
    # dirPath: 图片类的文件夹路径
    # 返回成功下载的图片数量
    def downloads(self, driver, name, dirPath):
        maxImgs = self.maxImages
        img_url_dic = self.img_url_dic
        img_desc_xpath = self.img_desc_xpath
        flog = self.flog
        
        # set timeout 
        socket.setdefaulttimeout(30)
        
        pos = 0
        i = 0
        
        # get total image that can download
        #imageNums = self.getTotalImages(driver)
       # print(str(imageNums))        
        if imageNums == 0:
            imageNums = self.maxImages
        
        # 计算已经下载的图片数量
        count = 0
        # 总共寻找到的图片数量
        total_count = 0
        print('Downloading', name)
        while (count < maxImgs):
            # 模拟滚动窗口以浏览下载更多图片
            pos += i * 500
            
            # 每隔10页需要点击加载更多图片
            if i > 0 and i % 10 == 0:
                try:
                    driver.find_element_by_id('pageMore').click()
                except ElementNotVisibleException as e:
                    flog.writelines("The pageMore is not currently visible.")
            i += 1
            js = "document.documentElement.scrollTop=%d" % pos
            driver.execute_script(js)
            
            resultLists = driver.find_elements_by_xpath(img_desc_xpath)
                        
            for img_desc_element in resultLists:
                total_count += 1
                try:
                    img_url = img_desc_element.get_attribute('data-objurl')
                except StaleElementReferenceException as e:
                    flog.write("{}".format(e.message))
                    continue
                
                img_desc = img_desc_element.get_attribute('data-title')
                img_ext = img_desc_element.get_attribute('data-ext')
                img_width = img_desc_element.get_attribute('data-width')
                img_height = img_desc_element.get_attribute('data-height')
                img_desc = self.filter_filename_str(img_desc)
                
                # 设置图片的宽和高的条件
#==============================================================================
#                 if int(img_width) < 500 or int(img_height) < 500:
#                     print("图片太小，不符合要求")
#                     break
#==============================================================================
                
                if img_url != None and not img_url in img_url_dic:
                    img_url_dic[img_url] = ''
                    ext = img_ext
                    # set the name of image
                    imageName = str(self.classes) + '_' + str(count) + '.' + ext
                    imagePath = os.path.join(dirPath,imageName)
                    #print("imagePath: {}".format(imagePath))
                    
                    # 判断图片是否已经存在
                    if os.path.isfile(imagePath):
                        count += 1
                        continue
                    
                    try:
                         #urllib.urlretrieve(img_url, imagePath)
                        # urlopen = urllib.URLopener()
                        # fp = urlopen.open(img_url)
                        # 下载图片
                        fp = urllib.request.urlopen(img_url)
                        data = fp.read()
                        # 清除并以二进制写入
                        imageFile = open(imagePath, 'wb')
                        imageFile.write(data)
                        imageFile.close()
                        
                        sizes = os.path.getsize(imagePath)
                        flog.writelines("%s %s %s\n" % (imagePath, str(sizes), img_url))
                       # print("width = {0}, height = {1}".format(img_width,img_height))
                        # 统计成功下载图片的数量
                        count += 1
                        time.sleep(5)
                        print('class ' + str(self.classes) + ', finish ' + str(count))
                    except IOError as e:
                        flog.writelines("%s %s %s\n" % (imagePath,e,img_url))
                        print("Fail download %s ... Error %s" % ( img_url,e))
                
                # 设置退出循环的条件：下载完目标数量
                if count >= maxImgs or total_count >= imageNums:
                    break
        return count

    def launch(self):
        # launch driver
        driver = webdriver.Firefox()
        driver.maximize_window()
        print(self.url)
        driver.get(self.url)
        assert '百度图片' in driver.title
        
        # 转换成传统翻页模式
#==============================================================================
#         pageModel_xpath = "//div[@id='userInfo']/a[1]"
#         pageModelElement = driver.find_element_by_xpath(pageModel_xpath)
#         pageModelElement.click()
#==============================================================================
        
        classFile = self.txtFile
        classNames = []
        with open(classFile,'r') as fr:
            classNames = fr.readlines()

        searchNames = self.getSearchNames()
        lens = len(searchNames)
        results = {}
        # 判断保存的目录是否存在
        if not os.path.isdir(self.imageFilePath):
            os.mkdir(self.imageFilePath)        
        
        for idx in range(lens):
            if idx <= 3 or idx == 5:
                continue
            elem = driver.find_element_by_name('word')
            name = searchNames[idx].strip()
            # 创建保存的图片类的文件夹
            imageDir = self.create_folder(classNames[idx])
            
            searchContent = name
            elem.send_keys(searchContent)
            elem.send_keys(Keys.RETURN)
            #assert unicode(name) in driver.title
            
            # start to download the image
            self.classes = idx
            downloadImgs = self.downloads(driver, name, imageDir)
            info = name + ' has downloads ' + str(downloadImgs) + ' images.'
            print(info)
            results[name] = downloadImgs
            self.classes += 1
            # clear the content of the search box
            elem = driver.find_element_by_name('word')
            elem.clear()
        
        print('Done!')
        driver.close()
        
        # print the final result
        totalImgs = 0
        for key, value in results.items():
            print(key + ': ' + str(value))
            totalImgs += value
        print('There are ' + str(self.classes) + ' classes' + \
                ', total Images are ' + str(totalImgs))
    
    # filter invalid characters in filename
    def filter_filename_str(self, s):
        invalid_set = ('\\', '/', ':', '*', '?', '"', '<', '>', '|', ' ')
        for i in invalid_set:
            s = s.replace(i, '_')
        return s
        
    # get total imags that can download
    def getTotalImages(self, driver):
        xpath = "//div[@id='pageMoreWrap']/div[1]"        
        
        # 因为需要寻找的元素的display=none，必须修改其display，使其可以定位到
        #if not driver.find_element_by_xpath(xpath).is_displayed():
        js = "var q = document.getElementById('resultInfo'); q.style.display='block'; "
        driver.execute_script(js)
        time.sleep(3)        
        
        resultInfo = driver.find_element_by_xpath(xpath)
        # transfer unicode to string
        info = str(resultInfo.text)
        print(info)
        
        imageNums = ''
        for i in info:
            if str.isdigit(i):
                imageNums += i
        if imageNums == '':
            return 0
        else:
            return int(imageNums)        
        
if __name__ == '__main__':
    crawler = Crawler()
    crawler.launch() 

