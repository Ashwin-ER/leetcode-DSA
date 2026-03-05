# Last updated: 05/03/2026, 08:00:22
1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        n = len(nums)
8        nums.sort()
9        for i in range(n):
10            return nums[0]
11
12