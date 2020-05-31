# -*- coding: utf-8 -*

# 递归, 很容易超过时间限制
class Solution1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if (m == 0 or n == 0):
            return max(m, n)
        
        if word1[m - 1] == word2[n - 1]:
            return self.minDistance(word1[0: m - 1], word2[0: n - 1])
        else:
            min1 = self.minDistance(word1[0: m - 1], word2[0: n]) + 1
            min2 = self.minDistance(word1[0: m], word2[0: n - 1]) + 1
            min3 = self.minDistance(word1[0: m - 1], word2[0: n - 1]) + 1

            return min(min1, min2, min3)
        

# word1 = "dinitrophenylhydrazine"
# word2 = "benzalphenylhydrazone"
# num = Solution().minDistance(word1, word2)
# print(num)
import numpy as np

class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        
        matrix = np.zeros(shape = (n + 1, m + 1))
        print(matrix)
        # 建立矩阵
        for i in range(1, m + 1): # 1 ~ m
            matrix[0][i] = i
        for j in range(1, n + 1): # 1 ~ n
            matrix[j][0] = j
        """
        [
            [0. 1. 2. 3. 4. 5.]
            [1. 0. 0. 0. 0. 0.]
            [2. 0. 0. 0. 0. 0.]
            [3. 0. 0. 0. 0. 0.]
        ]
        """
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[j - 1] == word2[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    min1 = matrix[i][j - 1] + 1
                    min2 = matrix[i - 1][j] + 1
                    min3 = matrix[i - 1][j - 1] + 1
                    matrix[i][j] = min(min1, min2, min3)
        print(matrix)         
        return matrix[n][m]

Solution().minDistance('a', 'b')
