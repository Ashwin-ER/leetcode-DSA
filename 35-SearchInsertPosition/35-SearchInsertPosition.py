# Last updated: 04/03/2026, 13:36:16
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

"""class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
            while i not nums:
                nums.append(i)
                nums.sort()
                if nums[i] == target:
                    return i"""