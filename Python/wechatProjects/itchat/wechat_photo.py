#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/24 9:31
@Author  : cai
@file    : wechat_photo.py
@concat  : 429546420@qq.com
@site    :
@software: PyCharm Community Edition
@desc    :

微信好友头像拼接
"""
import itchat
import math
import PIL.Image as Image
import os
import photomosaic as pm


def save_head_photo(save_photo_dir):
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()
    friends = itchat.get_friends(update=True)[1:]

    # 采集好友头像并保存到本地
    num = 0
    for fri in friends:
        img = itchat.get_head_img(userName=fri['UserName'])
        img_path = os.path.join(save_photo_dir, str(num) + '.jpg')
        if not os.path.exists(img_path):
            file_image = open(img_path, 'wb')
            file_image.write(img)
            file_image.close()
        num += 1

    print('完成好友头像保存至路径: ', save_photo_dir)


def create_photo_wall(save_photo_dir):
    head_imgs = os.listdir(save_photo_dir)
    print('微信好友数量: {}'.format(len(head_imgs)))

    ls = os.listdir(save_photo_dir)
    # 画布大小
    image_size = 1280
    # 算出每张图片的大小多少合适
    each_size = int(math.sqrt(float(image_size * image_size) / len(ls)))
    # 每行图片数量
    lines = int(image_size / each_size)
    print('each_size={}, lines={}'.format(each_size, lines))
    # 创建 1280*1280 的画布
    image = Image.new('RGBA', (image_size, image_size))
    x = 0
    y = 0

    for i in range(0, len(ls)):
        try:
            img_path = os.path.join(save_photo_dir, str(i) + ".jpg")
            # print('{} img: {}'.format(i, img_path))
            img = Image.open(img_path)
        except IOError:
            print("Error for image: {}".format(img_path))
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))  # 粘贴位置
            x += 1
            if x == lines:  # 换行
                x = 0
                y += 1

    image.save(os.path.join(os.getcwd(), "好友头像拼接图.jpg"))
    print('Finish!')


def create_photomosaic(save_photo_dir, background_photo):
    # 读取背景图片
    bg_photo = pm.imread(background_photo)
    # 读取好友头像图片，定义图片库
    pool = pm.make_pool(os.path.join(save_photo_dir, '*.jpg'))
    # 制作 50*50 的拼图马赛克
    image = pm.basic_mosaic(bg_photo, pool, (50, 50))
    # 保存结果
    pm.imsave('马赛克好友头像图片.jpg', image)


def main():
    '''
    处理入口
    :return:
    '''
    save_result_path = os.path.join(os.getcwd(), 'photo')
    if not os.path.exists(save_result_path):
        os.makedirs(save_result_path)
    print('save result path: {}'.format(save_result_path))
    # 保存好友头像
    save_head_photo(save_result_path)
    # 生成好友头像墙
    create_photo_wall(save_result_path)
    # 生成蒙太奇马赛克风格的好友头像墙
    # create_photomosaic(save_result_path, 'mosaic_bg.jpg')


if __name__ == '__main__':
    main()
