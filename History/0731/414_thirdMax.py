# -*- coding: utf-8 -*

"""
给定一个非空数组，返回此数组中第三大的数。
如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
- 不允许有重复
- 没有就返回第二大的

Given a non-empty array of integers, 
return the third maximum number in this array. 
If it does not exist, return the maximum number. 
The time complexity must be in O(n).
"""

# ======= 1. ===========
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 去重  data = [6, 2, 1, 3, 4, 1, 10]
        # list.count(2) 方法用于统计某个元素在列表中出现的次数
        # L = filter(lambda i: nums.count(i) == 1, nums)
        O = {}
        for i in nums:
            O[i] = ''
        L = O.keys()
        # 排序 倒序排序, 去三个数
        L = sorted(L, reverse=True)
        if len(L) > 3:
          L = L[0:3]
        # 输出最后一个
        if len(L) == 0: 
          return None
        return L[-1]

Solution().thirdMax([1, 1])

# ======= 2. ===========
class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # set(nums): 集合（set）是一个无序的不重复元素序列
        # 1. 去重set(xxx) 2. 排序  3. 序列
        L = list(sorted(set(nums), reverse = True))
        if len(L) >= 3:
            return L[:3][-1]
        elif len(L) == 0:
            return None
        else:
            return L[-1]


Solution1().thirdMax([5, 5, 5, 2, 3, 1, 2])
