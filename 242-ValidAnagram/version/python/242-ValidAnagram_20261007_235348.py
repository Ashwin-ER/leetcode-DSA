# Last updated: 07/10/2026, 23:53:48
1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        # Sort both strings and compare them
9        return sorted(s) == sorted(t)
10
11# Create instance and call the method
12solution = Solution()
13s = "anagram"
14t = "nagaram"
15result = solution.isAnagram(s, t)
16print(result)  # Output: True