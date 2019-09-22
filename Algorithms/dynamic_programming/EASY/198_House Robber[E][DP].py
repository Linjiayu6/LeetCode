# -*- coding: utf-8 -*

"""
https://leetcode-cn.com/problems/house-robber/

如果两间相邻的房屋在同一晚上被小偷闯入,系统会自动报警.

[1,2,3,4,5]
是选择1,3还是1,4的问题 (因为你选择1,5 最后还是1,3,5最大)
每个子问题都是间隔1个还是2个的问题

跟爬楼梯问题是一样的, 是选择一步还是两步的问题, 只不过换了一种方式
公式: L(n) = f(n) + max(f(n-1), f(n-2))
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        if not nums: return 0
        if _len < 2: return max(nums)
        if _len == 3: return max(nums[0] + nums[2], nums[1])
        _max, L = 0, nums[0:2] + [0] * (_len - 2)
        for i in range(2, _len):
            L[i] = nums[i] + max(L[i - 2], L[i - 3])
        return max(L)