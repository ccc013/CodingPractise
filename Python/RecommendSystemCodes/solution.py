#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/2/10 21:33
@Author  : cai
一个推荐系统代码练习，使用的数据集是GroupLens提供的MovieLens数据集
"""
import random,  math
import operator

def splitData(data, M, k, seed):
    """
    将数据集随机分成训练集和测试集的过程
    :param data:
    :param M:
    :param k:
    :param seed:
    :return:
    """
    test = []
    train = []
    random.seed(seed)
    for user, item in data:
        if random.randint(0, M) == k:
            test.append([user, item])
        else:
            train.append([user, item])
    return train, test

def Recall(train, test, N):
    """
    计算召回率
    :param train:
    :param test:
    :param N:
    :return:
    """
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += len(tu)
    return hit / (all * 1.0)

def Precision(train, test, N):
    """
    计算准确率
    :param train:
    :param test:
    :param N:
    :return:
    """
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += N
    return hit / (all * 1.0)

def GetRecommendation(user, N):
    pass

def Coverage(train, test, N):
    """
    计算覆盖率，表示最终的推荐列表中包含多大比例的物品
    :param train:
    :param test:
    :param N:
    :return:
    """
    recommend_items = set()
    all_items = set()
    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            recommend_items.add(item)
    return len(recommend_items) / (len(all_items) * 1.0)

def Popularity(train, test, N):
    """
    计算新颖度，这里用推荐列表中物品的平均流行度度量推荐结果的新颖度
    :param train:
    :param test:
    :param N:
    :return:
    """
    item_popularity = dict()
    for user, items in train.items():
        for item in items.keys():
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1
    ret = 0
    n = 0
    for user in train.keys():
        rank = GetRecommendation(user, N)
        for item, pui in rank:
            # 对物品的流行度取对数是在取对数后，流行度的平均值更加稳定
            ret += math.log(1 + item_popularity[item])
            n += 1
    ret /= n * 1.0
    return ret

# 计算余弦相似度
def calcUserSimilarity1(train):
    w = dict()               # 相似度矩阵
    for u in train.keys():
        for v in train.keys():
            if u != v:
                su = set(train[u].keys())
                sv = set(train[v].keys())
                if u not in w:
                    w[u] = dict()
                if v not in w[u]:
                    w[u][v] = 0
                w[u][v] = len(su & sv) / math.sqrt(len(train[u]) * len(train[v]))
    return w

# 采用稀疏矩阵优化计算相似度矩阵
def calcUserSimilarity2(train):
    itemUsers = dict()       # 物品-用户倒排表
    n = dict()              # 用户喜欢的物品数
    w = dict()              # 相似度矩阵
    # 建立倒排表
    for u, items in train.items():
        for i in items.keys():
            if i not in itemUsers:
                itemUsers[i] = set()
            itemUsers[i].add(u)
    # 计算相似度
    for i, users in itemUsers.items():
        for u in users:
            if u not in n:
                n[u] = 0
            n[u] += 1
            for v in users:
                if u != v:
                    if u not in w:
                        w[u] = dict()
                    if v not in w[u]:
                        w[u][v] = 0
                    w[u][v] = w[u].get(v, 0) + 1
    for u in w:
        for v in w[u]:
            w[u][v] /= math.sqrt(n[u] * n[v])
    return w

# UserCF推荐算法
def recommend(user, train, w, k):
    rank = dict()           # 推荐结果
    # 对目标用户user的相似度矩阵进行降序排序
    su = sorted(w[user].items(), key=operator.itemgetter(1), reverse=True)
    # print(su)
    # 找出前K个兴趣最接近的用户
    for v, wuv in su[:k]:
        # print(train[v])
        for i, rvi in train[v].items():
            if i not in train[user].keys():           # 排除已经有过反馈的物品
                if i not in rank:
                    rank[i] = 0
                # rank[i] += wuv * rvi, 因为rvi = 1
                rank[i] += wuv
    return rank

# 测试用例
train = {'A': {'a': {}, 'b': {}, 'd': {}},
         'B': {'a': {}, 'c': {}},
         'C': {'b': {}, 'e': {}},
         'D': {'c': {}, 'd': {}, 'e': {}}}
# 计算用户间的相似度
print('Calc user Similarity: ')
# w1 = calcUserSimilarity1(train)
# print('similarity1:')
# for user1, user2 in w1.items():
#     for u2, sim in user2.items():
#         print('%s%s--similarity = %s' % (user1, u2, sim))
w2 = calcUserSimilarity2(train)
# print('similarity2: ')
# for user1, user2 in w2.items():
#     for u2, sim in user2.items():
#         print('%s%s--similarity = %s' % (user1, u2, sim))
# 测试UserCF推荐算法
print('test user %s' % 'A')
rank = recommend('A', train, w2, 3)
print('recommend item is', rank.keys())
print('interests is ', rank.values())



