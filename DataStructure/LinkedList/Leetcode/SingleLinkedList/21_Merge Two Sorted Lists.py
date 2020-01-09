
"""
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
cur1, cur2
1. 分别遍历 list1+list2
2. 排序
3. 重新创建
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1

        cur1, cur2, List = l1, l2, []
        
        while cur1 is not None:
            List.append(cur1.val)
            cur1 = cur1.next
        while cur2 is not None:
            List.append(cur2.val)
            cur2 = cur2.next

        List = sorted(List)
        head = ListNode(List[0])
        curNew = head
        for val in List[1:]:
            curNew.next = ListNode(val)
            curNew = curNew.next
        return head


"""
双指针方法
1 -> 2 -> 3
2 -> 3 -> 6

1. 初始化比较, val哪个值小, 结点插入
2. 一样的值, 插入两遍

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2 is not None:
            return l2
        if l1 is not None and l2 is None:
            return l1

        Head = ListNode(-1)
        temp = Head
        print Head, temp
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            elif l1.val > l2.val:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            else:
                temp.next = ListNode(l1.val)
                temp = temp.next
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
                l2 = l2.next
        
        if l1 is not None:
            temp.next = l1
        if l2 is not None:
            temp.next = l2
        return Head.next
