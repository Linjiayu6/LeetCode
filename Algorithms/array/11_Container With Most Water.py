"""
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

index: 0
- 1,8: min(1,8) * (1-0)
- 1,6: min(1,6) * (2-0)
- 1,2: min(1,2) * (3-0)
- 1,5: min(1,5) * (4-0)
"""

# run but exceed the time limit
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # double pointer
#         _max = 0
#         for i in range(0, len(height) - 1):
#             for j in range(i + 1, len(height)):
#                 _max = max(_max, min(height[i], height[j]) * (j - i))
#         return _max

# print Solution().maxArea([1,8,6,2,5,4,8,3,7])


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, _max = 0, len(height) - 1, 0
        while(i < j):
          d_i, d_j = height[i], height[j]
          # _max = max(_max, min(d_i, d_j) * (j - i))
          if d_i > d_j:
              _max = max(_max, d_j * (j - i))
              j -= 1
          else:
              _max = max(_max, d_i * (j - i))
              i += 1
        return _max
print Solution().maxArea([1,8,6,2,5,4,8,3,7])