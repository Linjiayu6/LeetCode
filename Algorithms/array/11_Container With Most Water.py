"""
求面积问题, 双指针
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 求面积问题, 双指针
        i, j = 0, len(height) - 1
        _max = 0
        while (i < j):
            area = min(height[i], height[j]) * (j - i)
            _max = max(area, _max)
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1

        return _max

print Solution().maxArea([1,8,6,2,5,4,8,3,7])