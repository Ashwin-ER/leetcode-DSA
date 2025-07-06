class Solution (object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        prefix_map = { 0:1 }
        for n in nums:
            prefix_sum = prefix_sum + n
            if prefix_sum - k in prefix_map:
                count = count + prefix_map[prefix_sum - k]
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return count