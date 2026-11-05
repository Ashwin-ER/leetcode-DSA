# Last updated: 05/11/2026, 20:29:44
1class Solution(object):
2    def dailyTemperatures(self, temperatures):
3        """
4        :type temperatures: List[int]
5        :rtype: List[int]
6        """
7        n = len(temperatures)
8
9        answer = [0] * n
10
11        stack = []
12
13        for i in range(n):
14
15            while stack and temperatures[i] > temperatures[stack[-1]]:
16
17                prev = stack.pop()
18
19                answer[prev] = i - prev
20
21            stack.append(i)
22
23        return answer
24        