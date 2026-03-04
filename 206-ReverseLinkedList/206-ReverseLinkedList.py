# Last updated: 04/03/2026, 13:35:35
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        cur = head

        while cur:
            temp = cur.next 
            cur.next = prev
            prev = cur 
            cur = temp
        return prev
