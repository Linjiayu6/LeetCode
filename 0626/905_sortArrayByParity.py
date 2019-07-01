# -*- coding: utf-8 -*
"""
给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
你可以返回满足此条件的任何数组作为答案。
"""

def sortArrayByParity(A):
  i = 0 
  j = len(A) - 1
  while(True):
    # 找到偶数前进
    while(A[i] % 2 == 0):
      i = i + 1
    # 找到奇数前进
    while(A[j] % 2 != 0): 
      j = j - 1

    A[i], A[j] = A[j], A[i]
    i = i + 1
    j = j - 1

    if (i > j):
      return A

print(sortArrayByParity([3,1,2,4]))