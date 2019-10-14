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

"""
depth = 0
1. root is not None: depth = 1
2. root.left root.right 各作为结点 重复1步骤
   结果 = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


eg:
    1
   /\
  2  3
 / \
4   5

depth = 1
- H(2) = max(H(4), H(5)) + 1
- H(4) = 1
- H(5) = 1
- H(3)  = 1
- H(1) = max(H(2), H(3)) + 1

每一个结点都是如此运算
root = max(root.left数量, root.right数量) + 1
"""