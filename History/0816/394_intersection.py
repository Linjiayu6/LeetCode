# -*- coding: utf-8 -*

# 40 ms, 在所有 Python 提交中击败了85.74%的用户
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        return [9,4]
        """
        S1, S2 = set(nums1), set(nums2)
        L = []
        for i in S1:
            if i in S2:
                L.append(i)
        return L

print Solution().intersection([4,9,5], [9,4,9,8,4])
