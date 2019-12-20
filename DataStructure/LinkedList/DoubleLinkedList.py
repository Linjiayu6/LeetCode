#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Node:
    # None <= data => None
    def __init__ (self, data):
      self.data = data
      self.prev = None
      self.next = None

class DoubleLinkedList:

    def __init__ (self):
        # 头尾定义好了, self.__tail这个是和单链表不一样的地儿
        self.__head = None
        self.__tail = None

    def isEmpty (self):
        return self.__head is None

    def length (self):
        if self.isEmpty() is True:
            return 0
        cur, count = self.__head, 1
        while cur.next is not None:
          cur = cur.next
          count += 1
        return count

    """插入: 尾部"""
    """
    <= (head)n1 <=> n2 => None
    <= (head)n1 <=> n2 => n3 <=> None
    n2.next = n3
    n3.prev = n2
    """
    def insert_tail (self, data):
        newNode = Node(data)
        if self.isEmpty() is True:
            self.__head = newNode
            self.__tail = newNode
        else:
            # 从头开始插入
            # cur = self.__head
            # while cur.next is not None:
            #     cur = cur.next
            # cur.next = newNode
            # newNode.prev = cur

            # 从尾部开始插入
            self.__tail.next = newNode
            newNode.prev = self.__tail
            # 现在tail是 newNode
            self.__tail = newNode
            
    """插入: 头部"""
    """
    <= (head)n1 <=> n2 => None
    <= (head)n3 <=> n1 => n2 <=> None
    n3.next = self.__head
    self.__head.prev = n3
    self.__head = n3
    """
    def insert_head (self, data):
        newNode = Node(data)
        if self.isEmpty() is True:
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode

    """插入"""
    def insert (self, pos, data):
        if pos <= 1:
            self.insert_head(data)
        elif pos > self.length():
            self.insert_tail(data)
        else:
            cur, count = self.__head, 1
            # a <=> node(targetpos) <=> xxx <=> None
            # a <=> newnode <=> node(targetpos) <=> xxx <=> None
            while cur.next is not None:
                if pos - 1 == count:
                    newNode = Node(data)
                    newNode.next = cur.next
                    cur.next.prev = newNode
                    newNode.prev = cur
                    cur.next = newNode
                    break
                else:
                    cur = cur.next
                    count += 1

    """正向遍历"""
    def forward_traverse (self):
        L = []
        if self.isEmpty() is True:
            return L
        else:
            cur = self.__head
            while cur is not None:
                L.append(cur.data)
                cur = cur.next
            return L
    
    """反向遍历"""
    def reverse_traverse (self):
      L = []
      if self.isEmpty() is True:
            return L
      else:
          cur = self.__tail
          while cur is not None:
              L.append(cur.data)
              cur = cur.prev
          return L

    """删除: 头"""
    """
    (head)n1 <-> n2 <-> None
    (head)n2 <-> None
    """
    def delete_head (self):
        if self.isEmpty() is False:
            self.__head = self.__head.next
            self.__head.prev = None   
  
    """查询尾部节点的数据"""
    def get_tail_data (self):
      return self.__tail and self.__tail.data

def main():
  li = DoubleLinkedList()
  # insert
  li.insert_tail(10)
  li.insert_tail(20)
  li.insert_tail(30)
  li.insert(3, 666)
  li.insert_head(1)

  print li.length()
  print li.forward_traverse()
  print li.reverse_traverse()
  print li.get_tail_data()

if __name__ == "__main__":
    main()