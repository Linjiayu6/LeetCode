
# https://leetcode-cn.com/problems/rotate-matrix-lcci/

"""
Given matrix = 
[
  n = 3
  [1,2,3], [0][0] [0][1] [0][2] => [0][2] [1][2] [2][2] => [i][j] => [j][n - 1 - i]
  [4,5,6], [1][0] [1][1] [1][2] => [0][1] [1][1] [2][1]
  [7,8,9], [2][0] [2][1] [2][2] => [0][0] [1][0] [2][0]
],

Rotate the matrix in place. It becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
          return matrix
        
        n = len(matrix[0])
        if n == 0:
          return matrix

        # 矩阵赋值, 不能这么写 tempMatrix = [[0] * n] * m
        tempMatrix = [[0] * n for _ in range(m)]
        
        for i in range(m):
            data = matrix[i]
            for j in range(n):
                tempMatrix[j][n - 1 - i] = data[j]
        
        # 这里需要注意, 不能写成 matrix = tempMatrix
        matrix[:] = tempMatrix
        return matrix