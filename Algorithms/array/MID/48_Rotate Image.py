# # -*- coding: utf-8 -*
"""
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],      

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

i,j [0,0] - [0,2]
    [0,1] - [1,2]
    [0,2] - [2,2]

i,j [1,0] - [0,1]
    [1,1] - [1,1]
    [1,2] - [2.1]

i,j [2,0] - [0,0]
    [2,1] - [1,0]
    [2,2] - [2,0]

i = 0, 一行 [0, n - i] [1, n - i]
i = 1, 一行 [0, n - i] [1, n - i]
i = 2, 一行 ....
"""

# 使用了另外一个matrix的方法，但是不符合题中条件
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 行, 列
        n, m = len(matrix[0]), len(matrix)
        _matrix = []
        for _ in range(m):
          _matrix.append([0] * n)
        
        for i, _list in enumerate(matrix):
            for j, data in enumerate(_list):
                _matrix[j][n - 1 - i] = data

        matrix = _matrix
        return matrix

print Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])


"""
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

[0,0] => [0,3] => [3,3] => [3,0] => [0,0]
[0,1] => [1,3] => [2,3] => [2,0] => [0,1]
[0,2] => []
"""