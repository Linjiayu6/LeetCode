# 链表结构

[链表](https://www.ranxiaolang.com/static/python_algorithm/chapter3/index.html)
## 1. SingleLinkedList
[数据结构(五)之链表结构](https://www.jianshu.com/p/7a2d072a6c3e)

### 1.1 链表和数组区别?
数组可以存储多个元素, 但是缺点是
- **一段连续内存空间**
- 而且在数组的头或者中间插个数据的 *成本很高*, 需要大量的元素位移

链表也可存多个元素, 但**元素在内存中不必是连续的空间**, 对比数组有几个优点:
- **内存动态管理**, 因为不是连续的 
- 插入或删除数据时候, 时间复杂度可以达到O(1). 相对数组效率高很多。

链表缺点是: 访问任何一个必须从头开始访问, 直到找到对应的问题。
  
### 1.2 单向链表结构
(head)node -> node -> node -> null
- 链表的头是空或者第一个元素, 但是一旦头固定了, 不能变化, 变化的后续的指向。
- head其实就是链表的第一个结点。

### 1.3 单向链表操作
- 增加: 从头、从尾、从任意位置
- 删除: 从头、从尾、从任意位置
- 查询: 某值是否在链表中、遍历所有值
- 其他: 长度、是否为空
- 判断是否有 **环** 存在

### [1.4 链表中的双指针](https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/743/)
- 给定一个链表，判断链表中是否有环
- 解题思路1: 哈希表
- 解题思路2: 双指针技巧
```
一个快指针, 一个慢指针
一个安全的选择是每次移动慢指针一步，而移动快指针两步。每一次迭代，快速指针将额外移动一步。如果环的长度为 M，经过 M 次迭代后，快指针肯定会多绕环一周，并赶上慢指针。
```

## 2. DoubleLinkedList
[数据结构(六)之双向链表](https://www.jianshu.com/p/fb5a4169a618)

[Leetcode 双链表](https://leetcode-cn.com/explore/learn/card/linked-list/196/doubly-linked-list/756/)

### 2.1 结构、优缺点
- 结构: 见上参考链接
- (head)node1 <-> node2 <-> node3 <-> (tail)node4 <-> null
- 优点: 弥补单向链表的从头到尾遍历无法回到上一个结点的缺点。既可以从头到尾, 也可以从尾到头。
- 缺点: 删除或插入某个节点, 需要处理4个节点的引用; 内存空间占用大。

### 2.2 双向链表操作
**head、tail 标识, 操作和单向链表差不多, 注意双向指针的操作即可**
- [增加: 从头、从尾、从任意位置](https://leetcode-cn.com/explore/learn/card/linked-list/196/doubly-linked-list/757/)
- [删除: 从头、从尾、从任意位置](https://leetcode-cn.com/explore/learn/card/linked-list/196/doubly-linked-list/758/)
- 查询: 某值是否在链表中、遍历所有值、逆向遍历所有值
- 其他: 长度、是否为空
