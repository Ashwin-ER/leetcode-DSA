class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        if k==0: 
            return 0
        nums[:]=nums[n-k:]+nums[:n-k]
        return nums[:]