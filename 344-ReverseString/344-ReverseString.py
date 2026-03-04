# Last updated: 04/03/2026, 13:35:14
class Solution(object):
    def reverseString(self, s):
        #1
        """s[:] = s[::-1]
        return s"""

        #2
        left = 0
        right = len(s) -1
        while right > left:
            s[left], s[right] = s[right], s[left]
            right = right -1
            left = left +1
        #3
"""        return s.reverse()"""