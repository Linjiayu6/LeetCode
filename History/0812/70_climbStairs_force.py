# -*- coding: utf-8 -*

# 暴力解决问题
# 会超时 不是个好的解决方案
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int 
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

print Solution().climbStairs(4)