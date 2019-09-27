# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        L = []
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                L.append(node.val)

        if root is not None:
            postorder(root)

        return L