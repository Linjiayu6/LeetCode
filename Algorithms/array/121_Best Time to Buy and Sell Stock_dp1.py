"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.s
"""

# 超出时间了
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         _max = 0
#         _len = len(prices)
#         for i in range(0, _len):
#             for j in range(i + 1, _len):
#                 # day2: prices[j] day1: prices[i]
#                 if prices[j] - prices[i] > 0:
#                     _max = max(_max, prices[j] - prices[i])

#         return _max

# 超出时间了
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         _max = 0
#         for i, v1 in enumerate(prices):
#             for v2 in prices[i + 1:]:
#                 if v2 > v1:
#                     if _max < v2 - v1:
#                         _max = v2 - v1
            
#         return _max

# 最大值为: 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        _len = len(prices)
        if _len < 2: return 0

        _max = max(prices[1] - prices[0], 0)
        tmp = _max
        for i in range(1, _len - 1):
            R = prices[i + 1] - prices[i]
            _max = max(0, tmp, tmp + R, _max, R)
            tmp = max(tmp + R, R)
        return _max

print Solution().maxProfit([7,1,5,3,6,4])
