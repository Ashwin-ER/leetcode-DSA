# Last updated: 04/11/2026, 22:15:37
1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: List[int]
7        """
8
9        next_greater = {}
10        stack = []
11
12        for num in nums2:
13            while stack and num > stack[-1]:
14                smaller = stack.pop()
15                next_greater[smaller] = num
16
17            stack.append(num)
18        #stack = [4,2] , nxt_great={1: 3, 3: 4}
19        for num in stack:
20            next_greater[num] = -1
21        # next_greater = {1: 3, 3: 4} added {1: 3, 3: 4, 4:-1, 2:-1}
22        res=[]
23        for num in nums1:
24            res.append(next_greater[num])   
25        return res     
26