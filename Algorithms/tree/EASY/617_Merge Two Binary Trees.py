# 617. Merge Two Binary Trees
# https://leetcode-cn.com/problems/merge-two-binary-trees/

"""
1. 结点判断: t1且t2有值, t1 = t1 + t2, 并继续向下迭代
   t1.left = function(t1.left, t2.left)
   t1.right = function(t1.right, t2.right)
2. t1或t2有值, 只返回t1或t2
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            # 前序遍历, root -> left -> right
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        # 这里刚开始没有想明白
        if t1 or t2:
            return t1 if t1 else t2