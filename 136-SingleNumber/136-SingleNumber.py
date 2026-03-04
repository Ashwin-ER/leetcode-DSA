# Last updated: 04/03/2026, 13:35:47
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
