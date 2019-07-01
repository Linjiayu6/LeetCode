# -*- coding: utf-8 -*

"""
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, also in sorted non-decreasing order.
非递减顺序排序
平方后也需要非递减顺序排序

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

tips:
1. 负数平方后是需要重新排序;

(1) 内置方法
(2) 双指针方法
"""
def sortedSquares(A):
  separate = 0
  for i, d in enumerate(A):
    if d < 0 separate = i
    A[i] = d ** 2
  # 第一种: A = sorted(A)
  """
  第二种: 
    原正数 正序排序组 A[separate + 1, len(A)]
    原负数 倒序排序组 A[0, separate + 1]
  """
  positive = A[separate + 1, len(A)]
  negative = A[0, separate + 1]
  i = separate + 1
  j = separate
  List = []

  while(i < len(positive) and j >= 0):
    x = positive[i]
    y = negative[j]
    if x > y:
      List.append(y)
      j = j - 1
    else: 
      List.append(x)
      i = i + 1

    if (i == len(positive) - 1 or j = 0):
      List += positive[i:]
      List += negative[j:0:-1]

  print(List)
  return List


def sortedSquares(A):
  # while找到负数的位置
  N = len(A)
  j = 0
  while(p < N and A[p] < 0):
    j = j + 1

  # i 是 i--, j是 j++
  i = j - 1
  List = []
  while i >= 0 and j < N:
    if A[i]**2 < A[j]**2:
      List.append(A[i]**2)
      i = i - 1
    else:
      List.append(A[j]**2)
      j = j + 1
  
  while i >= 0:
    List.append(i)
    i = i - 1
  while j < N:
    List.append(j)
    j = j + 1

  return List
