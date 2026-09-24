# Last updated: 24/09/2026, 19:18:11
1class Solution(object):
2    def maxSubArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        current_sum = nums[0]
8        max_sum = nums[0]
9
10        for i in range(1, len(nums)):
11            current_sum = max(nums[i], current_sum + nums[i])
12            max_sum = max(current_sum, max_sum)
13        return max_sum
14
15        