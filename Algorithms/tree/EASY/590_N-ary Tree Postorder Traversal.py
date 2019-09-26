# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# For BST or BT, left -> right -> root
# For N-ary, children -> root
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def __init__(self):
        self.L = []

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is not None:
            self.traverse(root)

        return self.L
    
    def traverse(self, node):
        if node is not None:
            for child in node.children:
                self.traverse(child)
            self.L.append(node.val)