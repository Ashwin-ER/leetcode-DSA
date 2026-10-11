# Last updated: 11/10/2026, 12:33:23
1class Solution(object):
2    def runningSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7
8        num=0
9        L=[]
10        for i in range(len(nums)):
11            num = num + nums[i]
12            L.append(num)
13
14        return L
15
16