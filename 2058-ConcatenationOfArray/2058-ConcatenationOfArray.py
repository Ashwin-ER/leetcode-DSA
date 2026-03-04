# Last updated: 04/03/2026, 13:34:32
class Solution(object):
    def getConcatenation(self, nums):
        """return nums+nums"""
        n = len(nums)
        res = [0]*(2*n)
        for i in range(n):
            res[i]=nums[i]
            res[i+n]=nums[i]
        return res


 