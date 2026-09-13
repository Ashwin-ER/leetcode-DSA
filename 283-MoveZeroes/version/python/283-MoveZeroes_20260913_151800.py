# Last updated: 13/09/2026, 15:18:00
1class Solution(object):
2    def moveZeroes(self, nums):
3        zero_count = 0
4
5        # Move non-zero values forward
6        for i in range(len(nums)):
7            if nums[i] == 0:
8                zero_count += 1
9            else:
10                nums[i - zero_count] = nums[i]
11
12        # Add zeros at the end
13        for i in range(len(nums) - zero_count, len(nums)):
14            nums[i] = 0