# # -*- coding: utf-8 -*
# # 深度遍历
# """
# 从某一点出发, 依次放入栈中, 直到遍历到到某个深度后, 再无节点可走, 栈pop出去, 回退,
# 回退至前一个节点, 再去找其相邻的节点, 直到所有节点都遍历结束

# 从一个点开始
# - 1. 某节点node, 首先是判断在 _graph 图中是否已复制该节点, 没有复制的话, 去复制个新的走(3), 有的话走(2)
# - 2. 有该节点, 重复步骤(1)
# - 3. 复制该节点, 遍历该节点里面的相邻节点, 重复步骤(1)
# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, neighbors = []):
#         self.val = val
#         self.neighbors = neighbors

#     def _addchild(self, child):
#         self.neighbors.append(child)

# class Solution(object):
#     def cloneGraph(self, node):
#         """
#         :type node: Node
#         :rtype: Node
#         """
        