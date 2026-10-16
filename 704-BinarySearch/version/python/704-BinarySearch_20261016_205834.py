# Last updated: 16/10/2026, 20:58:34
1
2class Solution(object):
3    def search(self, nums, target):
4        left = 0
5        right = len(nums) - 1
6
7        while left <= right:
8            if nums[(left + right) // 2] < target:
9                left = (left + right) // 2 + 1
10
11            elif nums[(left + right) // 2] > target:
12                right = (left + right) // 2 - 1
13
14            else:
15                return (left + right) // 2
16
17        return -1
18