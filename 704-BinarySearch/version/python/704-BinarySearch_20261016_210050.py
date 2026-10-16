# Last updated: 16/10/2026, 21:00:50
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while(r>=l):
            m=(l+r)//2
            if(nums[m]==target):
                return m
            elif(target>nums[m]):
                l=m+1
            else:
                r=m-1
        return -1
    
        