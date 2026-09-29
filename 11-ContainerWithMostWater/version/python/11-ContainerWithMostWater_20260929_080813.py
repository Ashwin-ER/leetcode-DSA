# Last updated: 29/09/2026, 08:08:13
1class Solution(object):
2    def maxArea(self, height):
3        """
4        :type height: List[int]
5        :rtype: int
6        """
7        L = 0
8        R = len(height)-1
9        max_area = 0
10        while R>L:
11            area = (R-L) * min(height[L], height[R])
12            max_area = max(area, max_area)
13
14            if height[R]>height[L]:
15                L=L+1
16            else:
17                R=R-1
18        return max_area
19
20
21
22