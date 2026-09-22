# Last updated: 23/09/2026, 00:51:44
1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        result = [1] * len(nums)
8
9        left = 1
10
11        for i in range(len(nums)):
12            result[i] = left
13            left = left*nums[i]
14        
15        right = 1
16        for i in range(len(nums)-1,-1,-1):
17            result[i] *= right
18            right = right*nums[i]
19
20        return result