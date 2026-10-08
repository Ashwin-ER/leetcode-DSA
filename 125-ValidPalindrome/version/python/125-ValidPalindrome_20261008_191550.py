# Last updated: 08/10/2026, 19:15:50
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        res = ""
8        for ch in s:
9            if ch.isalnum():
10                res = res + ch.lower()
11        s = res
12
13        left = 0
14        right= len(s)-1
15
16        while right>=left:
17            if s[left] != s[right]:
18                return False
19
20            left = left +1
21            right = right -1
22        return True