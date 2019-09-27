# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.L = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is not None:
            self.traverse(root)
        return self.L
            
    def traverse(self, node):
        if node is not None:
              self.L.append(node.val)
              self.traverse(node.left)
              self.traverse(node.right)