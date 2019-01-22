#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/22 22:05
@Author  : cai

处理带有中文字符的文件
"""
import os
import codecs

def check_contain_chinese(check_str):
    '''
    判断是否包含中文字符
    :param check_str:
    :return:
    '''
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def process_file(input_file):
    datas = open(input_file, encoding='utf-8').read()
    print(datas)
    print(type(datas))
    str = '中'
    for val in datas:
        if check_contain_chinese(val):
            print(val)
            if val == str:
                print('{} equal {}'.format(val, str))


if __name__ == '__main__':
    print('start')
    input_file = 'E:\CodingPractise.git\Python\data\chinese_test.txt'
    process_file(input_file=input_file)
