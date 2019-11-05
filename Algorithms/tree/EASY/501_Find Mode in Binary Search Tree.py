# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.L = []
        
        def traverse(root):
            if root:
                self.L.append(root.val)
                traverse(root.left)
                traverse(root.right)
        
        traverse(root)

        # 求众数
        _num, _data = 0, []
        for i in list(set(self.L)):
            _tempNum = self.L.count(i)
            if _tempNum > _num:
                _data = [i]
                _num = _tempNum

            elif _tempNum == _num:
                _data += [i]

        return _data