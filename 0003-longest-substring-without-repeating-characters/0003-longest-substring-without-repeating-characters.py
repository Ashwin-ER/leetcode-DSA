class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        sett= set()
        longest = 0
        n = len(s)
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l = l +1
            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])
        return longest