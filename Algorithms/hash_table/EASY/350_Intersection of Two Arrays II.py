# # -*- coding: utf-8 -*
"""
两个数组重合的部分

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
"""

# 数据字典方法
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 少的创建hash表
        less, more = nums1, nums2
        if len(nums1) > len(nums2):
            less, more = nums2, nums1
        _dict = {}
        for i in less:
            if i not in _dict:
                _dict[i] = 1
            else:
                _dict[i] += 1
        
        L = []
        for i in list(set(less)):
            _count_less = _dict[i]
            _count_more = more.count(i)
            L += [i] * min(_count_less, _count_more)

        return L

print Solution().intersect([1,2,2,1], [2,2])


# 数组交集求解
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 去重的两个数组, 求交集, 再去每个nums里面求解最小的倍数
        _iter = set(nums1) & set(nums2)

        L = []
        for i in _iter:
            L += [i] * min(nums1.count(i), nums2.count(i))

        return L