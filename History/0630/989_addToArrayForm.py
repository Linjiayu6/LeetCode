# -*- coding: utf-8 -*

"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例 1：
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234
解释 2：

输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455
示例 3：

输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021
"""

def addToArrayForm(A, K):
  Str = ''
  for d in A: Str += str(d)
  # 455
  Str = str(int(Str) + K)
  A = list(Str)
  for i in range(len(A)): A[i] = int(A[i])
  return A
print(addToArrayForm([2,7,4], 181))

# 逐位相加
def addToArrayForm(A, K):
  # A的最后一位加上K, [2,7,185]
  A[-1] += K
  carry = 0
  for i in xrange(len(A) - 1, -1, -1):
    # divmod(a,b) -> (carry除数,下一个位置为余数)
    carry, A[i] = divmod(A[i], 10)
    if i: A[i - 1] += carry

  print(carry)
  if carry:
    A = map(int, str(carry)) + A
  return A

print(addToArrayForm([9,7,4], 281))