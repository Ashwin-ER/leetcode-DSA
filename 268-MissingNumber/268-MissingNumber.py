# Last updated: 04/03/2026, 13:35:20
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i
            res ^= nums[i]
        return res