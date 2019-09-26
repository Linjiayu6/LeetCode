"""
1. 遍历
2. 求递归的最大次数
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # from bottom to top, default value is 0
        if root is None:
            return 0
        
        _left_num = self.maxDepth(root.left)
        _right_num = self.maxDepth(root.right)

        return max(_left_num, _right_num) + 1