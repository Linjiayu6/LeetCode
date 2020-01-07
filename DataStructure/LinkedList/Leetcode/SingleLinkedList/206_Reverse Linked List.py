# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 遍历链表 获取List所有数据值
        List, cur = [], head
        while cur is not None:
            List.append(cur.val)
            cur = cur.next
        # 值反转
        List.reverse()

        # 遍历链表 变更数据
        i, curTemp = 0, head
        while curTemp is not None:
            curTemp.val = List[i]
            i += 1
            curTemp = curTemp.next
        return head

            