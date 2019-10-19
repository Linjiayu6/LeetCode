# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        self.L = []
        self.sum = sum
        if root is not None:
            root.val = [root.val]
            self.leaf(root)
        return self.L

    def leaf(self, root):
        if root is not None:
            # leaf
            if not root.left and not root.right:
                if sum(root.val) == self.sum:
                    print root.val
                    self.L.append(root.val)

            if root.left:
                print root.val, root.left.val
                root.left.val = root.val + [root.left.val]
                self.leaf(root.left)

            if root.right:    
                root.right.val = root.val + [root.right.val]
                self.leaf(root.right)

"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
"""
每一层都是一个array返回
          5
     /        \
  [5,4]      [5,8]
   /       /        \
[5,4,11] [5,8, 13]  [5,8, 4]
 /  \    / \
7    2  5   1

# root
  root.left and root.left.val = [root].append(root.left.val)
  root.right and root.right.val = [root].append(root.right.val)

  # 叶子节点
  if not root.left and not root.right:
      sum(root) == sum
        self.L.append(root)
"""

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
            # leaf
            if root.left is None and root.right is None:
                path.append(str(root.val))
                print path
                self.L.append(('->').join(path))

            create(root.left, path + [str(root.val)])
            create(root.right, path + [str(root.val)])

        create(root, [])
        return self.L