class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            prev, cur = cur, prev+cur
        return cur        