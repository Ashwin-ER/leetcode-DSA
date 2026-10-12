# Last updated: 12/10/2026, 10:43:45
1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        left = 0
9        right = len(numbers)-1
10
11        for i in range(len(numbers)):
12            if numbers[left]+numbers[right] == target:
13                return [left+1, right+1]
14            elif numbers[left]+numbers[right] > target:
15                right=right-1
16            else:
17                left=left+1