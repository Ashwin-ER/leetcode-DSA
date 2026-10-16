# Last updated: 16/10/2026, 19:24:12
1class Solution(object):
2    def maxSubArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        curr_sum = nums[0]
8        max_sum = nums[0]
9
10        for i in range(1,len(nums)):
11            curr_sum = max(nums[i], curr_sum + nums[i])
12            max_sum = max(max_sum, curr_sum)
13
14        return max_sum