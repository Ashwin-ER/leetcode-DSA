class Solution(object):
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        for num in nums[1:]:
            max_current = max(num , max_current + num)
            max_global = max(max_current , max_global)
        
        return max_global
        