"""
1. 数组中的数值最大值, 位置为i, root.val = List[i]
2. 数组被分为两个部分 root.left[0: i - 1] root.right[i + 1: len(List) - 1]
3. 继续迭代, 重复(1)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])

        if len(nums) > 1:
            _max = max(nums)
            _max_index = nums.index(_max)
            root = TreeNode(_max)
            root.left = self.constructMaximumBinaryTree(nums[0: _max_index])
            root.right = self.constructMaximumBinaryTree(nums[_max_index + 1: len(nums)])

            return root
        