class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''nums = [2,7,11,15]
        target = 9'''
        num = len(nums)
        for i in range(num):
            for j in range(i+1,num):
                if nums[i]+nums[j]==target:
                    #nums[i]+nums[j]
                    return [i,j]
        return []
        