# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """slow = fast = head

        while fast and fast.next:
            slow = head.next
            fast = head.next.next"""


        


        arr = []
        cur = head
        
        while cur:
            arr.append(cur)
            cur = cur.next
        
        return arr[len(arr) // 2]