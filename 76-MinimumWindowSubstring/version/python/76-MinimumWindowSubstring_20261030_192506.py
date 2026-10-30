# Last updated: 30/10/2026, 19:25:06
1class Solution(object):
2    def minWindow(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: str
7        """
8
9        left = 0
10        s_cnt = {}
11        t_cnt = {}
12        res = ""
13
14        if len(t) > len(s):
15            return ""
16
17        for right in range(len(t)):
18            if t[right] not in t_cnt:
19                t_cnt[t[right]] = 1
20            else:
21                t_cnt[t[right]] += 1
22
23        have = 0
24        need = len(t_cnt)
25        min_len = float("inf")
26
27        # Sliding window
28        for right in range(len(s)):
29
30            # Add character to window
31            if s[right] not in s_cnt:
32                s_cnt[s[right]] = 1
33            else:
34                s_cnt[s[right]] += 1
35
36            # Check required frequency
37            if s[right] in t_cnt and s_cnt[s[right]] == t_cnt[s[right]]:
38                have += 1
39
40            # Shrink window when valid
41            while have == need:
42
43                if right - left + 1 < min_len:
44                    min_len = right - left + 1
45                    res = s[left:right + 1]
46
47                # Remove left character
48                s_cnt[s[left]] -= 1
49
50                if s[left] in t_cnt and s_cnt[s[left]] < t_cnt[s[left]]:
51                    have -= 1
52
53                left += 1
54
55        return res