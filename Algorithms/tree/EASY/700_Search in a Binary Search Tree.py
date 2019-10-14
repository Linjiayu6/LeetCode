# 700. Search in a Binary Search Tree
# https://leetcode-cn.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is not None:
            if val > root.val:
                # 刚开始这里没有写对，因为没有写return
                return self.searchBST(root.right, val)
            elif val < root.val:
                return self.searchBST(root.left, val)
            else:
                return root

"""
Steps:
1. BST可以通过左右子树内容来判断剪枝
   广度优先搜索找到该值后
2. 减枝


- val < root.val 遍历Left Tree;
  val > root.val 遍历Right Tree;
  val == root.val return root
"""