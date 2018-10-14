#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/10/14 13:28
@Author  : cai

利用 wand 库实现简单的二维码关注图合成，包括添加文字或者图片
"""
from __future__ import print_function
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color
from wand.display import display
import os

FONT_DICT = {'宋体': 'songti.ttc',
             '微软雅黑1': 'msyh.ttc',
             '微软雅黑2': 'msyhbd.ttc',
             '微软雅黑3': 'msyhl.ttc'}


class ImageComposition(object):
    def __init__(self):
        pass

    # 画一个纯白背景，并保存
    def draw_bg(self, width, height, filename=None, color='white'):

        # with Image(width=width, height=height, background=Color(color)) as img:
        #     if filename is not None:
        #         img.save(filename=filename)
        img = Image(width=width, height=height, background=Color(color))
        if filename is not None:
            img.save(filename=filename)

        return img

    # 将图片 img 放在背景图片，并设置存放的位置
    def composite(self, img_back, img, left, top, save_name=None):
        with Image(filename=img_back) as w:
            with Image(filename=img) as r:
                with Drawing() as draw:
                    draw.composite(operator='atop',
                                   left=left, top=top,
                                   width=r.width,
                                   height=r.height,
                                   image=r)
                    draw(w)
                    display(w)
                    if save_name is not None:
                        w.save(filename=save_name)
        return w

    def composite_with_image(self, img_back, img, left, top, save_name=None, is_display=False):
        draw = Drawing()
        draw.composite(operator='atop',
                       left=left, top=top,
                       width=img.width,
                       height=img.height,
                       image=img)
        draw(img_back)
        if is_display:
            display(img_back)
        if save_name is not None:
            img_back.save(filename=save_name)
        return img_back

    def read_image(self, image_name):
        # with Image(filename=image_name) as img:
        img = Image(filename=image_name)
        print('width=', img.width)
        print('height=', img.height)
        print('size=', img.size)
        return img, img.width, img.height

    def resize(self, img, resize_width, resize_height, save_name=None):
        if type(img) == 'str':
            img = Image(filename=img)
        print('original size', img.size)
        img_clone = img.clone()
        img_clone.resize(resize_width, resize_height)
        if save_name is not None:
            img_clone.save(filename=save_name)
        return img_clone

    def draw_text(self, image, x, y, text, font_size=15, font_style='normal', font=None, text_alignment='left',
                  text_color='Black', filename=None, is_display=False):
        draw = Drawing()
        print('draw text={} in x={}, y={}'.format(text, x, y))
        if font is not None:
            draw.font = font
        draw.fill_color = Color(text_color)
        draw.font_size = font_size
        draw.font_style = font_style
        draw.text_alignment = text_alignment
        draw.text(x, y, text)
        draw(image)
        if is_display:
            display(image)
        if filename is not None:
            image.save(filename=filename)
        return image


if __name__ == "__main__":
    images_name = 'E:\CodingPractise.git\Python\Fun_Project\image_composition\qrcode_258.jpg'
    image_composition_cl = ImageComposition()
    # 先读取二维码图片，根据图片创建背景图片大小
    qrcode_img, width, height = image_composition_cl.read_image(images_name)
    print('QRcode image width={}, height={}'.format(width, height))
    bg_width = int(width * 2.5)
    bg_height = int(height * 1.1)
    print('background width={}, height={}'.format(bg_width, bg_height))
    bg = image_composition_cl.draw_bg(bg_width, bg_height, color='white', filename='background.jpg')
    # 将二维码图片和背景图片组合
    left = 5
    top = int((bg_height - height) // 2)
    # composite_images = image_composition_cl.composite('background.jpg', images_name, left=left, top=top,
    #                                                   save_name='composition.jpg')
    composite_images = image_composition_cl.composite_with_image(bg, qrcode_img, left=left, top=top,
                                                                 save_name='composition.jpg')
    # 添加图片
    # timg_name = 'E:\CodingPractise.git\Python\Fun_Project\image_composition\\timg.jpg'
    # timg, timg_width, timg_height = image_composition_cl.read_image(timg_name)
    # resize_width, resize_height = 300, 200
    # print('resize (width, height)= ', resize_width, resize_height)
    # timg_resize = image_composition_cl.resize(timg, resize_width, resize_height, 'timg_resize.jpg')
    # left_timg = width + left + 10
    # top_timg = int((bg_height - resize_height) // 2)
    # print('left_timg={}, top_timg={}'.format(left_timg, top_timg))
    # composite_images2 = image_composition_cl.composite_with_image(composite_images, timg_resize, left=left_timg,
    #                                                              top=top_timg,
    #                                                              save_name='composition2.jpg')
    # 添加文字
    text1 = 'Hello world'
    print(type(text1))
    text2 = 'wechat:机器学习与计算机视觉'
    text3 = '微信公众号: AI_Developer'
    text4 = '学习笔记，实战项目，分享交流'
    x = int(width * 1.5) + 50
    margin = 60
    y2 = int(bg_height // 2)
    y1 = y2 - margin
    y3 = y2 + margin
    y4 = y3 + margin - 20
    x1 = x2 = x3 = x + 20
    x4 = x + 20
    result1 = image_composition_cl.draw_text(composite_images, x1, y1, text1, font_size=20, text_color='Gray',
                                             text_alignment='center',
                                             font=None, filename='qrcode_composition.jpg',
                                             is_display=False)
    result2 = image_composition_cl.draw_text(result1, x2, y2, text2, font_size=30, text_color='Black',
                                             text_alignment='center',
                                             font=None, filename='qrcode_composition.jpg',
                                             is_display=False)
    # results = image_composition_cl.draw_text(result2, x3, y3, text3, font_size=20, text_color='Gray',
    #                                          text_alignment='center',
    #                                          font=None, filename='qrcode_composition.jpg',
    #                                          is_display=False)
    # results = image_composition_cl.draw_text(results, x4, y4, text4, font_size=25, text_color='Red',
    #                                          text_alignment='center',
    #                                          font=FONT_DICT['微软雅黑3'], filename='qrcode_composition.jpg',
    #                                          is_display=False)
