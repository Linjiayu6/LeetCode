class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)

        if m == 0 or n == 0:
            return max(m, n)

        else:
            # 建立矩阵
            # matrix = np.zeros(shape = (n + 1, m + 1))
            matrix = [[0] * (m + 1) for _ in xrange(n + 1)]
            # 建立矩阵
            for i in range(1, m + 1): # 1 ~ m
                matrix[0][i] = i
            for j in range(1, n + 1): # 1 ~ n
                matrix[j][0] = j
            
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if word1[j - 1] == word2[i - 1]:
                        matrix[i][j] = matrix[i - 1][j - 1]
                    else:
                        matrix[i][j] = min(
                            matrix[i - 1][j] + 1,
                            matrix[i][j - 1] + 1
                        )
            return matrix[n][m]