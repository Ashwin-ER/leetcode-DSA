# Last updated: 04/03/2026, 13:34:23
class Solution:
    def countDigits(self, num):
        count = 0
        for i in str(num): #1,2,3
            if int(num)%int(i) == 0: # 123%i
                count = count+1
        return count