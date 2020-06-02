class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        """
        [
          [ 1, 2, 3 ],
          [ 4, 5, 6 ],
        ]
        
        m = 2 n = 3

        [0][0]
        [0][1] [1][0]
        [1][1] [0][2]
        [1][2]
        """
        m = len(matrix)
        L = []
        for i in range(m):
          L.append(i)
        L += []