# Last updated: 19/10/2026, 22:56:50
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        left = 0
9        right = len(nums) - 1
10        while left <= right:
11            mid = (left + right) // 2
12            if nums[mid] == target:
13                return mid
14            if nums[left] <= nums[mid]:
15                if nums[left] <= target < nums[mid]:
16                    right = mid - 1
17                else:
18                    left = mid + 1
19            else:
20                if nums[mid] < target <= nums[right]:
21                    left = mid + 1
22                else:
23                    right = mid - 1
24        return -1
25
26        