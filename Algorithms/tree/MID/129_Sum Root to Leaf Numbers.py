# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.L = []
        self.pathLeaf(root, [])
        return sum(self.L)

    def pathLeaf(self, root, path = []):
        if root is None:
            return
        # leaf
        if root.left is None and root.right is None:
            path.append(str(root.val))
            self.L.append(int(''.join(path)))
            return 

        self.pathLeaf(root.left, path + [str(root.val)])
        self.pathLeaf(root.right, path + [str(root.val)])


"""
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""


"""
- 所有从root到leaf路径获取
- ['4', '9', '5'] - join() -> int()
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.pathLeaf(root, '')
        return self.sum

    def pathLeaf(self, root, path = ''):
        if root is None:
            return
        # leaf
        if root.left is None and root.right is None:
            path += str(root.val)
            self.sum += int(path)
            return 

        self.pathLeaf(root.left, path + str(root.val))
        self.pathLeaf(root.right, path + str(root.val))