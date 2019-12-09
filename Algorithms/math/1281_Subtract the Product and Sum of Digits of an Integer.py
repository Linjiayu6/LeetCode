# -*- coding: utf-8 -*

"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
链接：https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
Input: n = 234

Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
"""
class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        _sum, _product = 0, 1
        for string in list(str(n)):
            _sum += int(string)
            _product *= int(string)
        return _product - _sum

print Solution().subtractProductAndSum(1001)