# Last updated: 04/03/2026, 13:35:18
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        L=1
        R=n
        while R>L:
            M=(L+R)//2
            if isBadVersion(M):
                R=M
            else:
                L=M+1
        return L