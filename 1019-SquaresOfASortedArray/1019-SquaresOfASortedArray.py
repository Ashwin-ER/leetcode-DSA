# Last updated: 04/03/2026, 13:34:40
class Solution(object):
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        return sorted(nums)
