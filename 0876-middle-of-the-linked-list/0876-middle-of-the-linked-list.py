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
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow


        """cur = head.next 
        l =0

        while cur:
            l = l+1
            """





        


        """arr = []
        cur = head
        
        while cur:
            arr.append(cur)
            cur = cur.next
        
        return arr[len(arr) // 2]"""