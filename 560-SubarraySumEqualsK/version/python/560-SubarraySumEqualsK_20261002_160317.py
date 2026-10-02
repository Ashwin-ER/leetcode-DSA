# Last updated: 02/10/2026, 16:03:17
1class Solution(object):
2    def subarraySum(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        
9        count =0
10        prefix = 0
11        prefix_count ={0:1}
12
13        for num in nums:
14            prefix = prefix +num
15
16            needed = prefix - k
17
18            if needed in prefix_count:
19                count = count + prefix_count[needed]
20            
21            prefix_count[prefix] = prefix_count.get(prefix,0)+1
22        return count 