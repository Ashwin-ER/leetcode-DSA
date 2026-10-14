# Last updated: 14/10/2026, 13:21:19
1class Solution(object):
2    def findMaxAverage(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: float
7        """
8        window_sum = sum(nums[:k])
9        max_sum = window_sum
10
11        for i in range(k, len(nums)):
12            window_sum = window_sum - nums[i-k] + nums[i]
13            max_sum = max(max_sum, window_sum)
14        return float(max_sum)/k