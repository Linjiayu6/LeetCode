# -*- coding: utf-8 -*
"""
给定一个矩阵 A， 返回 A 的转置矩阵。
矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
示例 2：
输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]
"""
def transpose(A):
  # 行, 列
  row, col = len(A), len(A[0])

  i, j = 0, 0
  # A[i][j] = B[j][i] 需要建立一个维度确认的空矩阵
  B = []
  for _ in xrange(col):
    B += [[None] * row]

  # 需要转置: i为行( < col), j为列( < row)
  while(i < col):
    while(j < row):
      print(j, i, A[j][i])
      B[i][j] = A[j][i]
      j += 1
    i += 1
    j = 0

  return B

print(transpose([[1,2,3],[4,5,6]]))