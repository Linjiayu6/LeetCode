# -*- coding: utf-8 -*

"""
496. 下一个更大元素 I
- num1 遍历
- 在num1的x值, 对应在num2的位置的值+1为y值或者为空
- x < y return y; else -1;
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L = []
        nums2_len = len(nums2) - 1
        for val1 in nums1:
            default = -1
            for val2 in nums2[nums2.index(val1):]:
                if val2 > val1:
                    default = val2
                    break
            L.append(default)
        return L

print Solution().nextGreaterElement([2,4], [1,2,3,4])