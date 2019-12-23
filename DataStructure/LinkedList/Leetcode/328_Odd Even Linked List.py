# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
将奇偶数位置排在一起
偶数位置为 1,5.4
奇数位置为 1,3,6,7

1,3,6,7,1,5.4
"""

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        oddList, evenList = [], []
        cur, flag = head, 1
        while cur is not None:
            if flag % 2 == 0:
                evenList.append(cur.val)
            else:
                oddList.append(cur.val)
            flag += 1
            cur = cur.next
        
        List = oddList + evenList
        _index, _cur = 0, head
        while _index < len(List):
            _cur.val = List[_index]
            _cur = _cur.next
            _index += 1

        return head