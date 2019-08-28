# -*- coding: utf-8 -*
"""
C(N) = C(N - 1) + C(N - 2)

执行用时: 16 ms, 在所有 Python 提交中击败了93.82%的用户
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int 
        """
        Dict = dict(zip([1, 2], [1, 2]))
        if (n > 2):
          i = 3
          while(i <= n):
              Dict[i] = Dict[i - 1] + Dict[i - 2]
              i += 1
        return Dict.get(n)
        

print Solution().climbStairs(4)
