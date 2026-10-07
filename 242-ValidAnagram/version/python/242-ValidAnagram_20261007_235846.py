# Last updated: 07/10/2026, 23:58:46
1class Solution(object):
2
3    def isAnagram(self, s, t):
4
5        s = sorted(s)
6        t = sorted(t)
7
8        if len(s) != len(t):
9            return False
10
11        for i in range(len(s)):
12            if s[i] != t[i]:
13                return False
14
15        return True