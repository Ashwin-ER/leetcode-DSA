# Last updated: 04/03/2026, 13:35:21
class Solution(object):
    def addDigits(self, num):
        while num > 9:
            a = list(str(num))
            b = 0
            for i in a:
                b = b + int(i)
            num = b 
        return num
