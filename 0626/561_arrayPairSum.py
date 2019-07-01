# -*- coding: utf-8 -*

"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
使得从1 到 n 的 min(ai, bi) 总和最大。
输入: [1,4,3,2]

输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
"""
def arrayPairSum(nums):
  data = sorted(nums)
  i = 0
  SUM = 0
  # 排序
  while(i < len(data)):
    SUM += data[i]
    i += 2
  return SUM

print(arrayPairSum([-11, -14, 3, 2]))
