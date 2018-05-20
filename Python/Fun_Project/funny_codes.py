#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/5/20 9:23
@Author  : cai
一些有趣的代码
"""
import time


def express_love_simple():
    """
    简单的一行代码制作专属情人节爱心
    :return:
    """
    print('\n'.join([''.join([('AndyLove'[(x - y) % 8] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                                                                                                            x * 0.05) ** 2 * (
                                                                                                                                 y * 0.1) ** 3 <= 0 else' ')
                              for x in range(-30, 30)]) for y in range(15, -15, -1)]))


def express_love_advanced():
    words = input('Please input the words you want to say!:')
    # 例子：words = "Dear lili, Happy Valentine's Day! Lyon Will Always Love You Till The End! ♥ Forever!  ♥"
    for item in words.split():
        # 要想实现打印出字符间的空格效果，此处添加：item = item+' '
        # letterlist是所有打印字符的总list，里面包含y条子列表list_X
        letter_list = []
        for y in range(12, -12, -1):
            list__x = []  # list_X是X轴上的打印字符列表，里面装着一个String类的letters
            letters = ''  # letters即为list_X内的字符串，实际是本行要打印的所有字符
            for x in range(-30, 30):  # *是乘法，**是幂次方
                expression = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
                if expression <= 0:
                    letters += item[(x - y) % len(item)]
                else:
                    letters += ' '
            list__x.append(letters)
            letter_list += list__x
        print('\n'.join(letter_list))
        time.sleep(1.5)


def main():
    express_love_advanced()


if __name__ == '__main__':
    main()
