# -*- coding: utf-8 -*

"""
每次只能选择走一步还是两步, 每一个索引值代表当前能走的值

https://leetcode-cn.com/problems/min-cost-climbing-stairs/
cost = [10, 15, 20] output 15
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] output 16
"""

"""
fx = fx + min(fx-1, fx-2)
"""

# 44 ms, 在所有 Python 提交中击败了97.99%的用户
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost: return 0
        if len(cost) < 2: return min(cost)
        for i in range(2, len(cost)):
            # cost[i] += min(cost[i - 1], cost[i - 2])
            cost[i] += cost[i - 2] if cost[i - 1] > cost[i - 2]: else cost[i - 1]
        # return min(cost[-1], cost[-2])
        return cost[-1] if cost[-1] < cost[-2] else cost[-2]
