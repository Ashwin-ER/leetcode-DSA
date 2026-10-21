# Last updated: 21/10/2026, 14:52:07
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
11            width = R - L
12            area = width * min(height[R], height[L])
13
14            max_area = max(max_area, area)
15
16            if height[L] > height[R]:
17                R = R -1
18            else:
19                L = L +1
20        return max_area
21