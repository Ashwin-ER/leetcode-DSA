# Last updated: 05/03/2026, 08:17:11
1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        start, end = 0, len(nums)-1
8
9        
10        if not nums:
11           return 0
12
13        if nums[start]<nums[end]:
14            return nums[0]
15            
16        while nums[start]>nums[end]:
17            start=start+1
18        return nums[start]
19