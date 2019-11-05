# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.L = []
        def traverse(root):
            if root:
                traverse(root.left)
                self.L.append(root.val)
                traverse(root.right)
        traverse(root)

        # 排序, 去重也很重要, 例如返回的是[1,1] 这种排序是没有办法算出来的
        return (sorted(self.L) == self.L) and (len(list(set(self.L))) == len(self.L))
                

"""
中序遍历

(1) root.left.val
(2) root.val
(3) root.right.val

比较: (1) < (2) < (3) 条件
中序遍历是递增的
"""