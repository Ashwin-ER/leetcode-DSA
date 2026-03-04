# Last updated: 04/03/2026, 13:34:56
1class Solution(object):
2    def search(self, nums, target):
3        for i in range(len(nums)):
4            if nums[i] == target:
5                return i
6
7        return -1