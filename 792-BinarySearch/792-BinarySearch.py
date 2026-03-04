# Last updated: 04/03/2026, 13:34:48
class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid + 1
            else:
                right = mid -1
        return -1
                
        
        """for i in range(len(nums)):
            if nums[i]==target:
                return i
        else:
            return -1"""
            