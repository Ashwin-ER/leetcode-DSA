# Last updated: 13/09/2026, 15:34:10
1class Solution(object):
2    def moveZeroes(self, nums):
3        zero_count = 0
4
5        for i in range(len(nums)):
6            if nums[i] == 0:
7                zero_count += 1
8            else:
9                nums[i - zero_count] = nums[i]
10
11        for i in range(len(nums) - zero_count, len(nums)):
12            nums[i] = 0