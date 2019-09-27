# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        L = []
        
        def traverse(node):
            if node:
                traverse(node.left)
                L.append(node.val)
                traverse(node.right)
                         
        if root is not None:
            traverse(root)
        return L