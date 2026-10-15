# Last updated: 15/10/2026, 14:02:01
1class Solution(object):          
2    def subarraySum(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        
9        prefix_count = {0: 1}
10        prefix_sum = 0
11        count = 0
12        for num in nums:
13            prefix_sum = prefix_sum + num
14
15            if prefix_sum - k in prefix_count:
16                count = count + prefix_count[prefix_sum -k]
17            if prefix_sum not in prefix_count:
18                prefix_count[prefix_sum] = 0
19            prefix_count[prefix_sum] = prefix_count[prefix_sum] +1
20        return count