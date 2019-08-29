# -*- coding: utf-8 -*

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 可以是连续求解问题, 但是重点是, 
        # 1. 找到当前 买入的最小值 _min
        # 2. 收入最大值, 且需要对比 当前值 - _min, 因为每次都需要确认的是 小的值在list左侧, 大的值在list右侧
        # 3. _max
        if not prices: return 0
        _max, _min = 0, prices[0]
        for i in prices:
            _max = max(_max, i - _min)
            _min = min(_min, i)
        return _max

print Solution().maxProfit([7,1,5,3,6,4])
