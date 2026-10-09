# Last updated: 09/10/2026, 09:50:35
1class Solution(object):
2    def lengthOfLongestSubstring(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7
8        left = 0
9        seen = set()
10        max_len = 0
11
12        for right in range(len(s)):
13            while s[right] in seen:
14                seen.remove(s[left])
15                left =left +1
16            seen.add(s[right])
17            max_len = max(max_len, right-left+1)
18        return max_len
19
20
21        