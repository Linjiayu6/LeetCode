"""
589. N-ary Tree Preorder Traversal
https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# preorder traversal: root -> left -> right for BST
"""
root -> [A, B, C]
         A -> [x, xx, xxx]
"""
class Solution(object):
    def __init__(self):
        self.L = []

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return self.L
        else:
            self.tranverse(root)

    def tranverse(self, node):
        if node is not None:
            self.L.append(node.val)
            if node.children is not None:
                for child in node.children:
                    self.tranverse(child)