# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Input: -1->5->3->4->0
Output: -1->0->3->4->5

思路:
1. 获取所有值
2. 重新排序
3. 重新创建链表值
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
          return head
        List, cur = [], head
        # 1. get all values
        while cur is not None:
            List.append(cur.val)
            cur = cur.next
        # 2. sorted values
        List = sorted(List)
        
        self.head = ListNode(List[0])
        cur = self.head
        # 3. create singleList by sorted values
        for v in List[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return self.head
            