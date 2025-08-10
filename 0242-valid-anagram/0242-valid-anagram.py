class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        d1 = {}

        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        for i in t:
            if i in d1 and d1[i] > 0:
                d1[i] -= 1
            else:
                return False

        return True