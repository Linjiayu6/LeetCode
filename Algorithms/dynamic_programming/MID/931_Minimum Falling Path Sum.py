"""
[[1,2,3],[4,5,6],[7,8,9]]

ALL:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
https://leetcode-cn.com/problems/minimum-falling-path-sum

L[1][0] += min(L[0][0], L[0][1])
L[1][1] += min(L[0][0], L[0][1], L[0][2])
L[1][2] += min(L[0][1], L[0][2])

L[n][m] += min(L[n-1][m-1], L[n-1][m], L[n-1][m])
"""
class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        limit = len(A)
        if limit == 0:
            return A[0][0]
        for i in range(1, limit):
            for j in range(0, limit):
                if j == 0:
                    A[i][j] += min(A[i-1][j], A[i-1][j+1])
                elif j == limit - 1:
                    A[i][j] += min(A[i-1][j-1], A[i-1][j])
                else:  
                    A[i][j] += min(A[i-1][j-1], A[i-1][j], A[i-1][j+1])
        return min(A[-1])

print Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
