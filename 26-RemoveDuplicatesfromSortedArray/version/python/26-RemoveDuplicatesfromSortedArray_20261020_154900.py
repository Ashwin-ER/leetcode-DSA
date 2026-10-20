# Last updated: 20/10/2026, 15:49:00
1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        left = 0
8
9        for right in range(1, len(nums)):
10            if nums[left]!=nums[right]:
11                left = left+1
12                nums[left]=nums[right]
13        return left +1