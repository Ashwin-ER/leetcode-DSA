'''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = [1,1,2]
        n = len(nums)
        a = len(nums)-len(set(nums))
        if n!=set(nums):
            return list[set(nums) + a[:-1],end='_']
        else:
            return nums'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k