#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__ (self):
        self.__head = None

    """是否为空"""
    def isEmpty (self):
        return self.__head is None

    """返回链表长度"""
    def length (self):
        # cur移动遍历节点
        cur, count = self.__head, 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    """
    头插法: 在单链表头部插入一个节点. 注意: 头还是头, 只是指向变了
        (head)n1 => n2 => None
        (head)node => n1 => n2 => None
    """
    def insert_head (self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            newNode.next = self.__head
            self.__head = newNode

    """
    尾插法: 在单链表尾部增加一个节点
        (head)n1 => n2 => None
        (head)n1 => n2 => node => None
    """
    def insert_tail (self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    """在指定位置插入元素"""
    """
        (head)n1 => n2 => None
        (head)n1 => node => n2 => None
    """
    def insert (self, pos, data):
        # 头插入
        if pos <= 0:
            self.insert_head(data)
        # 尾插入
        elif pos >= self.length():
            self.insert_tail(data)
        else:
            """插入是在前一个节点插入"""
            newNode = Node(data)
            # cur => targetNode => xxx => None
            cur, count = self.__head, 0
            while count < pos - 1:
                cur = cur.next
                count += 1
            newNode.next = cur.next
            cur.next = newNode

    """删除: 头"""
    """ 
    * 头还是头, 是指针变化
    (head)n1 => n2 => n3 => None
    (head)n2 => n3 => None
    """
    def delete_head (self):
        if self.__head is not None:
            self.__head = self.__head.next

    """删除: 尾"""
    """
    (head)n1 => n2 => n3 => None
    (head)n1 => n2 => None
    """
    def delete_tail (self):
        if self.__head is not None:
            cur = self.__head
            # cur => target => None
            while cur.next is not None:
                if cur.next.next is None:
                    break
                cur = cur.next
            cur.next = None

    """删除: 指定位置"""
    def delete (self, pos):
        if pos <= 1:
            self.delete_head()
        elif pos >= self.length():
            self.delete_tail()
        else:
            cur, count = self.__head, 0
            # cur => target => xxx => None
            while count < pos - 2:
                cur = cur.next
                count += 1
            
            if cur.next is not None and cur.next.next is not None:
                cur.next = cur.next.next
            else:
                cur.next = None

    """遍历"""
    def traverse (self):
        L = []
        cur = self.__head
        while cur is not None:
            L.append(cur.data)
            cur = cur.next
        return L
    
    """查询某个节点"""
    def search (self, data):
        # (head)n1 => n2 => None
        if self.isEmpty() is False:
            cur = self.__head
            while cur is not None:
                if data == cur.data:
                    return True
                else:
                    cur = cur.next
            return False
        return False

def main():
    Li = SingleLinkedList()
    # 链表是否为空
    print '链表是否为空' + str(Li.isEmpty())

    # 增加节点
    Li.insert_head(100)
    Li.insert_head(200)
    Li.insert_tail(666)
    Li.insert_tail(777)

    # 此时长度
    print '此时长度' + str(Li.length())

    # 在某个位置上插入数据 [200, 100, 666, 777]
    Li.insert(0, 888)

    print '遍历:'
    print Li.traverse()
    # Li.delete_head()
    # Li.delete_tail()
    Li.delete(4)
    print '遍历:'
    print Li.traverse()

    print '检查是否存在某个值'
    print Li.search(1)

if __name__ == "__main__":
    main()
