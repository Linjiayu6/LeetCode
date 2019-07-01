
# -*- coding: utf-8 -*

"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。

示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
"""
def sortArrayByParityII(A):
  # i 偶数位置, j 奇数位置
  i = 0
  j = 1
  while(True):
    while i < len(A) and A[i] % 2 == 0: i += 2
    while j < len(A) and A[j] % 2 == 1: j += 2
    if i < len(A) and j < len(A):
      # 交换位置
      A[i], A[j] = A[j], A[i]
      i += 2
      j += 2
    else: 
      return A

print(sortArrayByParityII([4,2,5,7,5,2]))