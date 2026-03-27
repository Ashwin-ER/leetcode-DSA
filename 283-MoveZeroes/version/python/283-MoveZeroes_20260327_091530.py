# Last updated: 27/03/2026, 09:15:30
1class Solution(object):
2    def moveZeroes(self, nums):
3        a = 0 
4
5        for i in range(len(nums)):
6            if nums[i] != 0:
7                nums[a], nums[i] = nums[i], nums[a]
8                a = a + 1
9
10        return nums
11
12            