class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        n = len(nums)
        for i in range(n):
            num = nums[i]
            complement = target - num
            if complement in nums_map:
                return [nums_map[complement], i] 
            nums_map[num] = i 
