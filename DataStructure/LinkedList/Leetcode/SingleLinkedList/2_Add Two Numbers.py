# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Input: (2 -> 5 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 1 -> 8
Explanation: 352 + 465 = 817.
https://leetcode-cn.com/problems/add-two-numbers

"""

# 暴力解题方法
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        List1, List2 = [], []
        while l1 is not None:
            List1.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            List2.append(str(l2.val))
            l2 = l2.next
        
        List1.reverse()
        List2.reverse()

        str1 = ''.join(List1)
        str2 = ''.join(List2)

        num = int(str1) + int(str2)
        L = list(str(num))
        L.reverse()
        
        Head = ListNode(int(L[0]))
        temp = Head
        for _data in L[1:]:
            node = ListNode(int(_data))
            temp.next = node
            temp = temp.next
        return Head