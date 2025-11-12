class Solution:
    def countDigits(self, num):
        count = 0
        for i in str(num): #1,2,3
            if int(num)%int(i) == 0: # 123%i
                count = count+1
        return count