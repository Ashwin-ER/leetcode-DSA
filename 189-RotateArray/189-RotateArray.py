# Last updated: 04/03/2026, 13:35:37
class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        if k==0: 
            return 0
        nums[:]=nums[-k:]+nums[:-k]
        return nums[:]