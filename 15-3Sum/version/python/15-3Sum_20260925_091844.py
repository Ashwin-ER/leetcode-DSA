# Last updated: 25/09/2026, 09:18:44
1class Solution(object):
2    def threeSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[List[int]]
6        """
7        nums.sort()
8        res = []
9
10        
11        for i in range(len(nums)):
12            if i > 0 and nums[i] == nums[i - 1]:
13                continue
14
15            L=i+1
16            R=len(nums)-1
17            
18            while R>L: 
19                total = nums[i] + nums[L] + nums[R]
20                if total==0:
21                    res.append([nums[i],nums[L], nums[R]])
22                    L=L+1
23                    R=R-1
24                    while R>L and nums[L]==nums[L-1]:
25                        L+=1
26                    while R>L and nums[R]==nums[R+1]:
27                        R-=1
28                elif total <0:
29                    L+=1
30                else:
31                    R-=1
32                
33        return res 
34