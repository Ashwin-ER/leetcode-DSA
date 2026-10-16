# Last updated: 16/10/2026, 20:47:22
1class Solution(object):
2    def search(self, nums, target):
3        left=0
4        right=len(nums)-1
5        
6        while left<=right:
7            mid=(left+right)//2
8            if nums[mid]==target:
9                return mid
10            elif nums[mid]<target:
11                left=mid + 1
12            else:
13                right = mid -1
14        return -1
15                
16        
17        """for i in range(len(nums)):
18            if nums[i]==target:
19                return i
20        else:
21            return -1"""
22            