# -*- coding: utf-8 -*

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
https://leetcode-cn.com/problems/climbing-stairs/

(1)
1.1 = 1

(2)
2.1 = (1.1) + 1
2.2 = 2

(3)
3.1 = (2.1 = (1.1) + 1) + 1
3.2 = (2.2) + 1
3.3 = (1.1) + 2

(4)
4.1 = (3.1) + 1
4.2 = (3.2) + 1
4.3 = (3.3) + 1
4.4 = (2.2) + 2
4.5 = (2.1) + 2

(5)
5.1 = (4.1) + 1
5.2 = (4.2) + 1
5.3 = (4.3) + 1
5.4 = (4.4) + 1
5.5 = (3.1) + 2
5.6 = (3.2) + 2
5.7 = (3.3) + 2

C(N) = C(N-1) + C(N-2)

执行用时 : 12 ms, 在所有 Python 提交中击败了98.74%的用户
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, q = 1, 2
        if n < 3:
            return n
        else:
            for __ in range(3, n + 1):
                p, q = q, p + q
            return q

print Solution().climbStairs(4)
