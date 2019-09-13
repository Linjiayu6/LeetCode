# -*- coding: utf-8 -*

"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
链接：https://leetcode-cn.com/problems/climbing-stairs
"""

"""
S1 = 1 = (1)
S2 = S1 + 1, 2 = (2)
S3 = S2 + 1, S1 + 2 = (2 + 1 = 3)
S4 = S2 + 2, S3 + 1 = (2 + 3 = 5)
...

Sn = Sn-2 + 2, Sn + 1
"""

"""
但for循环里面含range()，相对速度也会快些，while语句是纯粹用Python代码写成，所以速度最慢。
所以函数式编程最好使用内置函数，然后才考虑使用列表推导或for循环。最好不用while循环.
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        x, y = 2, 1
        for __ in range(3, n + 1):
            x, y = x + y, x
        return x
        
print Solution().climbStairs(5)