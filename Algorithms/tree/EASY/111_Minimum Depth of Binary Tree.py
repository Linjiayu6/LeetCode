# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 没有该结点
        if root is None:
          return 0
        left_num = self.minDepth(root.left)
        right_num = self.minDepth(root.right)
        # 如果左边或右边没有该结点, 只有一边有的话, 结论是 left_num + right_num + 1
        if root.left is None or root.right is None:
            return left_num + right_num + 1

        return min(left_num, right_num) + 1



"""
    1
   /\
  2  3
 / \
4   5

H1 = min(H2, H3) + 1
H2 = min(H4, H5) + 1 = 2
H4 = 1
H5 = 1

H3 = 1

H1 = min(H2, H3) + 1
H1 = min(2, 1) + 1 = 2

总结为: H1 = min(左边数量, 右边数量) + 1

该题有另外两个case是: 
1. 如果是没有该节点 return 0
2. 如果只有一边子树节点的话, 上面总结内容不是这样了
   1
    \ 
     2
    / \
   3   4
  这里最小的是3, 如果按照(总结为: H1 = min(左边数量, 右边数量) + 1) 就是2了 是不对的

  if root.left or root.right 有一个节点是空的话
    return left_num + right_num + 1
3. else: H1 = min(左边数量, 右边数量) + 1
"""