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

### 1 实现思路
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

## 2. Depth First Search
- DPS深度优先搜索包含前序、中序、后序
- [深度优先搜索](https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/7/)

### 2.1 前序遍历
- 根节点 -> 左子树 -> 右子树

### 2.2 中序遍历
- 左子树 -> 根节点 -> 右子树
```
# example
def tranverse_mid(node):
    if node is not None:
        tranverse_mid(node.left)
        _L_mid.append(node.val)
        tranverse_mid(node.right)
```

### 2.3 后序遍历
- 左子树 -> 右子树 -> 根节点

### 2.4 总结
- 理解树的结构, 结点有左子树和右子树;
- 从root结点开始从上至下去找具体的某个结点;
- 递归完成操作;
- 理解前序中序后序的遍历;

## 3. Breadth First Search
- 从上到下, 从左到右(层次遍历)
- [广度优先搜索](https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/8/)

```
思路: 
L = [] # 栈的层级代表该数的层级
level = 0 # 初始化该level为0

- 1. if len(L) == level: 新建个层级 L = [[]]
- 2. 数据: L[level].append(node.val)
- 3. 处理左子树, 和1,2步骤一样 唯一不同的是level + 1
-    处理右子树, 和1,2步骤一样 唯一不同的是level + 1
```

## 4.求解树的深度
- 转化为求解递归遍历的次数
```
def depth(node):
    # if node不为空
    if node is not None:
        a = depth(node.left)
        b = depth(node.right)
    else:
        return 0
    return max(a, b) + 1
```
