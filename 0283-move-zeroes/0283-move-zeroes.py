class Solution(object):
    def moveZeroes(self, nums):
        a = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[a], nums[i] = nums[i], nums[a]
                a = a + 1

        return nums

            
