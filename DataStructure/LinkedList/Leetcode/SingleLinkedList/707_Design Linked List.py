class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__head = None

    def isEmpty(self):
        return self.__head is None
        
    def length(self):
        if self.isEmpty() is True:
            return 0
        else:
            cur = self.__head
            count = 1
            while cur.next is not None:
                count += 1
                cur = cur.next
            return count

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.isEmpty() is True:
            return -1
        if self.length() <= index:
            return -1
        _index = 0
        cur = self.__head
        while cur is not None:
            if _index == index:
                return cur.val
            else:
                _index += 1
                cur = cur.next


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        n = Node(val)
        if self.isEmpty() is True:
            self.__head = n
        else:
            n.next = self.__head
            self.__head = n


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index <= 0:
            self.addAtHead(val)
        elif self.length() <= index:
            self.addAtTail(val)
        else:
            cur = self.__head
            _index = 0
            n = Node(val)
            # 1 -> 3 -> None
            while cur.next is not None:
                # Here is easy to be wrong
                if _index == index - 1:
                    n.next = cur.next
                    cur.next = n
                    break
                else:
                    _index += 1
                    cur = cur.next


    def deleteHead(self):
        if self.isEmpty() is False:
            self.__head = self.__head.next
    
    def deleteTail(self):
        if self.isEmpty() is False:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = None

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index <= 0:
            self.deleteHead()
        elif index >= self.length():
            self.deleteTail()
        else:
            cur = self.__head
            _index = 0
            while cur.next is not None:
                # Here is easy to be wrong
                if _index == index - 1:
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next
                    _index += 1