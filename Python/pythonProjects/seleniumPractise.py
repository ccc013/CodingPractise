# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:51:33 2015

@author: cai
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

txtFile = '/home/cai/dataset/foodIngredients/' + 'food-40.txt'
names = []
with open(txtFile) as fr:
    names = fr.readlines()
    strs = '-'.join(names).strip()
    names = strs.split('-')

print len(names)

driver = webdriver.Firefox()
driver.maximize_window()
url = 'http://image.baidu.com/'
driver.get(url)
assert '百度图片' in driver.title


for i in range(2):
    elem = driver.find_element_by_name('word')
    keywords = names[i].strip()
    elem.send_keys(unicode(keywords))
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    print 'ok!'
    
    img_desc_xpath = '//ul/li[@class="imgitem"]'
    desc_element = driver.find_element_by_xpath(img_desc_xpath)
    
    img_desc = desc_element.get_attribute('data-title')
    img_url = desc_element.get_attribute('data-objurl')
    
    print img_desc
    print img_url
    
    # clear the content
    elem = driver.find_element_by_name('word')
    elem.clear()

#==============================================================================
# ext = img_url.split('.')[-1]
# filename = '/home/cai/dataset/test/' + '0.' + ext
# urllib.urlretrieve(img_url, filename)
#==============================================================================

#driver.close()