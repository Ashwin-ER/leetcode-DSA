class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        maxi = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                cnt = cnt +1
                maxi = max(maxi, cnt)
                
            else:
                cnt = 0
        return maxi
                
        