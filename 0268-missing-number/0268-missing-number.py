class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i
            res ^= nums[i]
        return res