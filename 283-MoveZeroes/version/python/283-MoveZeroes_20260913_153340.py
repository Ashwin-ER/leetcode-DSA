# Last updated: 13/09/2026, 15:33:40
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        