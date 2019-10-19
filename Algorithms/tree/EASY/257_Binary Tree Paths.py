# https://leetcode-cn.com/problems/binary-tree-paths/


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.L = []
        def create(root, path=[]):
            if root is None:
                return
            path.append(root.val)
            # leaf
            if root.left is None and root.right is None:
                self.L.append(('->').join(path))

            create(root.left, path)
            create(root.left, path)
        
        create(root, [])
        return self.L



"""
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

(1) root is not None, path = [root.val]
(2) not root.left and not root.right 叶子结点
       return L += path.join('->')
(3) 左右子树调用
"""