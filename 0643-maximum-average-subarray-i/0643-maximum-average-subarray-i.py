class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k

        Final = sum(nums[left:right])

        CurrentSum = Final

        while right < len(nums):
            CurrentSum = CurrentSum - nums[left] + nums[right]
            if CurrentSum > Final:
                Final = CurrentSum
            left+=1
            right+=1

        return Final/k