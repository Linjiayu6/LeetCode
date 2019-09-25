# -*- coding: utf-8 -*

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 1. 创建一个BST
def binary_insert(root, node):
    # 没有该Node结点, 则新建该结点
    if root is None:
        root = node
        return root

    # 判断是要在左tree, 还是右tree
    """
    root.left 或 root.right是否为空
    (1) 空: 直接插入该点
    (2) 不为空: 去接下来找空的点插入
    """
    # 判断node.val值 < root.val, 在左侧, 否则在右侧
    if node.val < root.val:
        if root.left is None:
            root.left = node
        else:
            binary_insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            binary_insert(root.right, node)

root = TreeNode(3) 
binary_insert(root, TreeNode(5))
binary_insert(root, TreeNode(1))
binary_insert(root, TreeNode(7))
print root.val

#    3
#  /   \
# 1     5
#        \ 
#         7

# print the whole nodes of tree

# 2. 打印所有的结点值
nodeList = []
def Print(node):
    if node is not None:
        nodeList.append(node.val)
        if node.left is not None:
            Print(node.left)
        # else:
        #     nodeList.append(None)

        if node.right is not None:
             Print(node.right)
        # else:
        #     nodeList.append(None)
Print(root)
print nodeList


# 3. 遍历
"""
1. 前序遍历
root -> left -> right
"""
_L = []
def tranverse(node):
    if node is not None:
        _L.append(node.val)
        tranverse(node.left)
        tranverse(node.right)
          

"""
2. 中序遍历
left -> root -> right
"""
_L_mid = []
def tranverse_mid(node):
    if node is not None:
        tranverse_mid(node.left)
        _L_mid.append(node.val)
        tranverse_mid(node.right)
        
tranverse_mid(root)
print _L_mid

"""
3. 后序遍历
left -> right -> root
"""
_L_post = []
def tranverse_post(node):
    if node is not None:
        tranverse_post(node.left)
        tranverse_post(node.right)
        _L_post.append(node.val)

tranverse_post(root)
print _L_post
