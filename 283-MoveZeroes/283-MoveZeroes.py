# Last updated: 04/03/2026, 13:35:17
class Solution(object):
    def moveZeroes(self, nums):
        a = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a = a + 1

        return nums

            
