# -*- coding: utf-8 -*
"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

输入: coins = [1, 5, 11], amount = 15
输出: 3 
解释: 5 * 3
"""
# def coinChange(coins, amount):
#   i = len(coins) - 1
#   List = []
#   coins = sorted(coins)
#   print(coins)

#   # 从i开始
#   while(i > -1):
#     total = amount
#     j = i
#     sub_total = 0
#     detail = []
#     # 从i开始的往前找数据
#     while(j > -1):
#       if coins[j] > total and total != 0:
#         j -= 1
#       else:
#         # 11 除数, 余数 15 / 11 = (1, 4) 一张11元 4元是剩下的钱
#         carry, total = divmod(total, coins[j])
#         detail.append(str(carry) + ' * ' + str(coins[j]))
#         print(detail, total)
#         # 一张11元
#         sub_total += carry

#         if total > 0:
#           j -= 1
#         else:
#           print('value of final', sub_total, detail)
#           List += [sub_total, detail]
#           sub_total = 0
#           total = amount
#           detail = []
#           break
#     i -= 1

#   print(List)
#   # if (len(List.keys()) < 1):
#   #   return -1
#   # return sorted(List.keys())[0]
# print(coinChange([186,419,83,408], 6249))
