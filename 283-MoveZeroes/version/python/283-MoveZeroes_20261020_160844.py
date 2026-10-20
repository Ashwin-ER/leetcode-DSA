# Last updated: 20/10/2026, 16:08:44
1class Solution(object):
2    def moveZeroes(self, nums):
3        left = 0
4        for right in range(len(nums)):
5            if nums[right]!=0:
6                nums[left], nums[right] = nums[right], nums[left]
7                left = left +1
8        return nums