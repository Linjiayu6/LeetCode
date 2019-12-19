# 链表结构

[数据结构(五)之链表结构](https://www.jianshu.com/p/7a2d072a6c3e)

## 1. 链表和数组区别?
数组可以存储多个元素, 但是缺点是 
- **一段连续内存空间**
- 而且在数组的头或者中间插个数据的 *成本很高*, 需要大量的元素位移

链表也可存多个元素, 但 **元素在内存中不必是连续的空间**, 对比数组有几个优点: 
- 内存动态管理, 因为不是连续的 
- 插入或删除数据时候, 时间复杂度可以达到O(1). 相对数组效率高很多。

链表缺点是: 访问任何一个必须从头开始访问, 直到找到对应的问题。
  
## 2. 链表结构
(head)node -> node -> node -> null
- 链表的头是空或者第一个元素, 但是一旦头固定了, 不能变化, 变化的后续的指向。
- head其实就是链表的第一个结点。

## 3. 链表操作
- 增加: 从头、从尾、从任意位置
- 删除: 从头、从尾、从任意位置
- 查询: 某值是否在链表中、遍历所有值
- 其他: 长度、是否为空