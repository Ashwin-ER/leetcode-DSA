# Last updated: 28/10/2026, 15:28:04
1class Solution(object):
2    def characterReplacement(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: int
7        """
8        count = {}
9        left = 0
10        max_freq = 0
11        longest = 0
12
13        for right in range(len(s)):
14            ch = s[right]
15
16            # Count the new character
17            count[ch] = count.get(ch, 0) + 1
18
19            # Highest frequency seen in the current window
20            max_freq = max(max_freq, count[ch])
21
22            # Shrink if too many replacements are needed
23            window_length = right - left + 1
24
25            if window_length - max_freq > k:
26                count[s[left]] -= 1
27                left += 1
28
29            # Record the longest window
30            longest = max(longest, right - left + 1)
31
32        return longest
33