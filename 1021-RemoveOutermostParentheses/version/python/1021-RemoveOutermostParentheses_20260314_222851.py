# Last updated: 14/03/2026, 22:28:51
1class Solution(object):
2    def removeOuterParentheses(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        ans = ""
8        cnt = 0
9
10        for char in s:
11            if cnt == 0 and char == '(':
12                cnt += 1
13            elif char == '(':
14                cnt += 1
15                ans += char
16            elif cnt == 1 and char == ')':
17                cnt -= 1
18            else:
19                cnt -= 1
20                ans += char
21
22        return ans