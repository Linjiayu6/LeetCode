# class Solution(object):
#     # [1,2,3,8,9,10]
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         _len = len(A)
#         # list length
#         if _len < 3:
#             return 1
#         # every element is the same or have negative and positive number
#         if A[0] == A[1] or A[0] > A[-1]:
#             return 1
#         # distance A[1] - A[0] == 2
#         if A[1] - A[0] > 1:
#             return (_len * (_len - 1)) / 2
#         if A[1] - A[0] == 1:
#             return (_len * (_len - 1)) / 2 - (_len - 1)

# print Solution().numberOfArithmeticSlices([1, 3, 5, 7])
