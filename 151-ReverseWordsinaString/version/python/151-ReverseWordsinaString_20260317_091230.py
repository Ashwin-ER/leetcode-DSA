# Last updated: 17/03/2026, 09:12:30
1class Solution(object):
2    def reverseWords(self, s):
3        words = s.split()
4        r_words = " ".join(words[::-1])
5
6        return r_words