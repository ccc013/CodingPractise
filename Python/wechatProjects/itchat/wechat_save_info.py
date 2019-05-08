#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/30 19:06
@Author  : luocai
@file    : wechat_save_info.py
@concat  : 429546420@qq.com
@site    : 
@software: PyCharm Community Edition 
@desc    :

保存你的好友数量、关注公众号数量、群聊数量信息
"""
import itchat
import os
import pandas as pd

# 好友获取的信息内容, 分别是性别、昵称、备注、签名、省份、城市
friend_key = ['Sex', 'NickName', 'RemarkName', 'Signature', 'Province', 'City']
# 公众号获取的信息内容，分别是昵称、城市、城市、签名
mps_key = ['NickName', 'City', 'Province', 'Signature']


def get_info(save_file_path):
    '''
    获取公众号信息
    :param save_file_path:
    :return:
    '''
    # 避免频繁扫描二维码登录
    itchat.auto_login(hotReload=True)
    itchat.dump_login_status()
    # 获取好友信息
    we_friend = itchat.get_friends(update=True)[:]
    friends = we_friend[1:]
    total_numbers = len(friends)
    print('你的好友数量为: {}'.format(total_numbers))
    friend_infos_dict = {}
    for fri_info in friends:
        for key in friend_key:
            if friend_infos_dict.get(key, False):
                friend_infos_dict[key].append(fri_info[key])
            else:
                friend_infos_dict[key] = [fri_info[key]]
    # 保存信息
    fri_save_file_name = os.path.join(save_file_path, '好友信息.csv')
    df = pd.DataFrame(friend_infos_dict)
    df.to_csv(fri_save_file_name, sep=',')

    # 获取公众号信息
    mps = itchat.get_mps(update=True)
    mps_num = len(mps)
    print('你关注的公众号数量: {}'.format(mps_num))

    mps_save_file_name = os.path.join(save_file_path, '公众号信息.csv')
    mps_dict = {}
    for mp in mps:
        for key in mps_key:
            if mps_dict.get(key, False):
                mps_dict[key].append(mp[key])
            else:
                mps_dict[key] = [mp[key]]

    df = pd.DataFrame(mps_dict)
    df.to_csv(mps_save_file_name, sep=',', encoding='utf-8')


def main():
    '''
    处理入口
    :return:
    '''
    save_result_path = os.path.join(os.getcwd(), 'result')
    if not os.path.exists(save_result_path):
        os.makedirs(save_result_path)
    print('save result path={}'.format(save_result_path))
    get_info(save_result_path)
    print('Finish!')


if __name__ == '__main__':
    main()
