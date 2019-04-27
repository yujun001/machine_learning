# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 11:17
# @Author  : RIO
# @desc: 采草药0-1背包
'''
input_cuple表示多组数据，每组数据的体积及花费
'''
# code: utf-8
# 要求的最大体积
given_volume = 70
# 样本数上限
max_items = 101
# 体积上限
max_volume = 1001
# 每组样本体积及花费
input_cuple = [(71, 100), (69, 1), (1, 2)]


########################################################二维的情况#######################################################
# 动规数组
dp_2 = [[0] * max_volume for i in range(max_items)]
# 此处的动规数组为二维数组，下面会提出一种优化为一维的实现方法
def get_dp_2_dimensional():
    # i件物品
    for i in range(1, len(input_cuple) + 1):
        # j代表当前最大体积
        for j in range(max_volume):
            # 因为当前加入某件某品后可能会超过要求的体积，超出为0，否则为1
            is_beyond_volume = 1 if input_cuple[i - 1][0] <= j else 0
            # 状态转移方程
            dp_2[i][j] = max(
                dp_2[i - 1][j - is_beyond_volume * input_cuple[i - 1][0]] + is_beyond_volume * input_cuple[i - 1][1],
                dp_2[i - 1][j])


get_dp_2_dimensional()
print(dp_2[3][70])
for i in range(101):
    for j in range(1001):
        if dp_2[i][j]>0:
            print('i, j is {},{}'.format(i, j))
########################################################二维的情况#######################################################

########################################################一维的情况#######################################################

########################################################一维的情况#######################################################