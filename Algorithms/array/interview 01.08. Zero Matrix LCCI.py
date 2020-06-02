# https://leetcode-cn.com/problems/zero-matrix-lcci/
# -*- coding: utf-8 -*

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        如果[2][1]为0, 那么[2][:] 和 [:][1]都为0
        Input: 
        [
          [1,1,1],
          [1,0,1],
          [1,1,1]
        ]
        Output: 
        [
          [1,0,1],
          [0,0,0],
          [1,0,1]
        ]

        遍历有0的 位置记录为 i_set = (i1, i2), j_set = (j1, j2)
        那么操作矩阵 [i1][:] = 0 [:][j1] = 0
        """
        m = len(matrix)
        if (m == 0):
          return matrix
        if (m == 1 and len(matrix[0]) < 2):
          return matrix

        n = len(matrix[0])
        i_set, j_set = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    i_set.add(i)
                    j_set.add(j)

        for i in range(m):
          if i in i_set:
            matrix[i][:] = [0] * n
          for _j in j_set:
            matrix[i][_j] = 0
        return matrix

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))