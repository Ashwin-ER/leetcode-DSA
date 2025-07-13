class Solution(object):
    def reverseString(self, s):
        #1
        """s[:] = s[::-1]
        return s"""

        #2
        left = 0
        right = len(s) -1
        while right > left:
            s[right], s[left]= s[left], s[right]
            right = right -1
            left = left +1
        #3
"""        return s.reverse()"""