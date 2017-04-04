# -*- coding: utf-8 -*-
import sys,os,re
import urllib.request
import json,datetime


# an example of Baidu image search :http://image.baidu.com/i?ct=201326592&lm=-1&tn=result_pageturn&pv=&word=%E5%91%B5%E5%91%B5&z=0&pn=0&cl=2&ie=utf-8#pn=0
# dirname = input('Please choose where you want to store your picture\n(example: D:\\图片\\test ): ')
# content = input('Please input the content you want to search: ')
# num = input('Please input the amount of pictures(max=600): ')
dirname = 'D:\\图片\\test'
content = 'picture'
num = 60
url1 = "http://image.baidu.com/i?ct=201326592&lm=-1&tn=result_pageturn&pv=&word="
url2 = "&z=0&pn=0&cl=2&ie=utf-8#pn=0"
url3 = "&z=0&pn="
url4 = "&cl=2&ie=utf-8#pn=0"
if os.access(dirname,0):
        pass
else:
	os.makedirs(dirname)
count = 0
successcount = 0
flag = 1
logname=dirname+"ImageMessage.txt"#,"w"
flog=open(logname,"w")

starttime = datetime.datetime.now()

#下载图片
for i in range(10):
        if flag == 1:
            url = url1 + content + url3 + str(i*60) +url4
            # this only for python2.x
            # sock = urllib.urlopen(url)
            # python3.x
            print('url is {}'.format(url))
            try:
                result = urllib.request.urlopen(url) 
            except IOError as e:
                print('failed!')
                break
            else:
                ipdata = json.loads(result)
                if ipdata['data']:
                    for n in ipdata['data']:
                        if n and n['obj_url']:
                            try:
                                data_img = urllib.request.urlopen(n['obj_url']).read()
                            except IOError as e:
                                print('failed to download image: {}'.format(n['obj_url']))
                                break
                            else:
                                fpostfix = os.path.splitext(n['obj_url'])(1)
            
            reg=re.compile("(?<=objurl\":\")(http.*?\.(jpg|gif|png|bmp|jpeg|JPG))")#正则表达式匹配下载地址·
            html=result.read()
            results=reg.findall(html)
            if results:
                os.chdir(dirname)
                for one in results:

                   #统计
                    count=count+1
                    if (count>=num):
                       print("down loadfinish")
                       flag=-1
                       break
                   
                    imgeurl=one[0]
                    print("image:" , one[0])
                    #print imgeurl.rindex('.'),len(imgeurl)
                    succname = imgeurl[  int(imgeurl.rindex('.'))+1:int(len(imgeurl))]
                   
                    try:
                        savename=dirname + str(count) + "." + succname
                        downloadimge = urllib.request.urlopen(one[0])#, data, timeout)
                        f=open(savename,"wb")
                        f.write(downloadimge.read())
                        f.close()
                        
                        size=os.path.getsize(savename)
                        flog.writelines("%s %s %s" % (savename,str(size),one[0]))
                        print("Download Success")
                        successcount=successcount+1
                        
                    except BaseException as e:
                        flog.writelines("%s %s %s" % (savename,e,one[0]))
                        print("Fail download %s ... Error %s" % ( imgeurl,e))
                  


print("finished: (%s/%s) downloaded" % (str(successcount),str(num)))
endtime = datetime.datetime.now()
print((endtime-starttime).seconds)
flog.close()

