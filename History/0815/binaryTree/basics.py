# -*- coding: utf-8 -*

"""
由于python的基本变量类型中没有二叉树类型，因此要使用python实现二叉树的相关操作需要先自定义二叉树类
"""

# 树的结点
class treeNode:
    def __init__(self, val):
          self.val = val
          self.left = None
          self.right = None

"""
1. 创建结点 node
2. node.left = 操作1
3. node.right = 操作2

迭代处理: 操作1/2 再次创建结点
"""
def createTree(nodeList):
    # 数据
    if nodeList[0] != None:
        node = treeNode(nodeList[0])
        nodeList.pop(0)
        node.left = createTree(nodeList)
        node.right = createTree(nodeList)
    else:
        # 数据
        return nodeList.pop(0)
    # node是个root
    return node

root = createTree([10, 7, 4,None,None, 9,None,None, 13, None, 15,None,None])

"""
Root Val: 10
Root.left.val 7
Root.right.val 13
"""
print 'Root Val:', root.val
print 'Root.left.val', root.left.val
print 'Root.right.val', root.right.val


"""
1. 前序遍历
根节点, 左子树, 右子树
"""
def travel(root):
    L = []
    if root != None:
        L.append(root.val)
        L += travel(root.left)
        L += travel(root.right)
    else:
        return []

    return L

print travel(root)