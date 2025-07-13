class Solution(object):
    def reverseString(self, s):
        """s[:] = s[::-1]
        return s"""
        left = 0
        right = len(s) -1
        while right > left:
            s[right], s[left]= s[left], s[right]
            right = right -1
            left = left +1
        return s 