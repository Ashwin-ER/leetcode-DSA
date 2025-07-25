class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        window = set()
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L =L+1
            if nums[R] in window:
                return True
            window.add(nums[R]) 
        return False