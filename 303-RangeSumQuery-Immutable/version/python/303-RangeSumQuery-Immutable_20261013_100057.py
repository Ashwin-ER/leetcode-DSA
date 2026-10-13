# Last updated: 13/10/2026, 10:00:57
1class NumArray(object):
2
3    def __init__(self, nums):
4        """
5        :type nums: List[int]
6        """
7        self.prefix = [0]
8        for num in nums:
9            self.prefix.append(self.prefix[-1]+num)
10        
11
12    def sumRange(self, left, right):
13        """
14        :type left: int
15        :type right: int
16        :rtype: int
17        """
18        return (self.prefix[right+1]-self.prefix[left])
19        
20
21
22# Your NumArray object will be instantiated and called as such:
23# obj = NumArray(nums)
24# param_1 = obj.sumRange(left,right)