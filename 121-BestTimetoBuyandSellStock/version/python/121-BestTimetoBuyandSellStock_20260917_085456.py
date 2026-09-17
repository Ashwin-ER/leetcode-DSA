# Last updated: 17/09/2026, 08:54:56
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        minimum = prices[0]
8        answer = 0
9        for i in range(len(prices)):
10            minimum = min(prices[i], minimum)
11            answer = max(answer, prices[i] - minimum)
12        return answer