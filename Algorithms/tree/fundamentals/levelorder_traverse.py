"""
left -> right
top -> bottom

解题思路:
- level:0, if len(L) == level 说明可以新建一个层级放数据
- self.L[level].append(node.val)

- node.left 重复调用处理, 唯一不同的是level+1
- node.right 重复调用处理, 唯一不同的是level+1
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.L = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        def traverse(node, level):
            # 从1层开始, 初始化创建个新的
            if len(self.L) == level:
                self.L.append([])
            self.L[level].append(node.val)

            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)

        traverse(root, 0)
        return self.L