# Last updated: 04/11/2026, 00:31:39
1class Solution:
2    def isValid(self, s):
3        stack = []
4
5        pairs = {
6            ')': '(',
7            '}': '{',
8            ']': '['
9        }
10
11        for char in s:
12            if char in pairs:
13                if not stack:
14                    return False
15
16                if stack[-1] != pairs[char]:
17                    return False
18
19                stack.pop()
20
21            else:
22                stack.append(char)
23
24        return len(stack) == 0