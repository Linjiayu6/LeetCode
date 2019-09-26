# Tree

## Tips
```

            ┌ 普通树             ┌ 斜树(左斜树、右斜树)
            │                     │ 
      ┌ 树1 ┤ 二叉树(BinaryTree)  ┤ 满二叉树：树深 log(n+1)
      │     │                     │
      │     │                     └ 完全二叉树(重要)： 树深 [logn]+1         
      │     └ ...
      │
森林 ─┤ 树2
      │ ...
      │
      └
```

## 1. BST 二叉搜索树
- 每个节点比其左子树元素大，比其右子树元素小
```
- 例如:
   4
  / \
 2   5
      \  
       7
```

### 1.1 实现思路
```
root = createNode(value)
node创建并结点插入到root中
(1) function(root, node)
(2) node.val < root.val, 插入到左子树中
    (2.1) root.left 是否为None, None则 root.left = node
    (2.2) 则递归调用该函数, 找到可以插入的点, 执行(1)
(3) node.val >= root.val, 插入到右子树中
    (2.1) root.right 是否为None, None则 root.right = node
    (2.2) 则递归调用该函数, 找到可以插入的点, 执行(1)
```

### 1.2 前序遍历
- 根节点 -> 左子树 -> 右子树

### 1.3 中序遍历
- 左子树 -> 根节点 -> 右子树
```
# example
def tranverse_mid(node):
    if node is not None:
        tranverse_mid(node.left)
        _L_mid.append(node.val)
        tranverse_mid(node.right)
```

### 1.4 后序遍历
- 左子树 -> 右子树 -> 根节点

### 总结
- 理解树的结构, 结点有左子树和右子树;
- 从root结点开始从上至下去找具体的某个结点;
- 递归完成操作;
- 理解前序中序后序的遍历;

