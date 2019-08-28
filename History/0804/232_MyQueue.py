# -*- coding: utf-8 -*

"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
"""
class MyQueue(object):
  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.Queue.append(x)
        return self.Queue
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.Queue.pop(0)


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.Queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.Queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(2)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()