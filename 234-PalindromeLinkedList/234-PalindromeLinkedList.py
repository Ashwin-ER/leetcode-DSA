# Last updated: 04/03/2026, 13:35:25
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        arr = []


        while head:
            arr.append(head.val)
            head = head.next

        return arr == arr[::-1]

            