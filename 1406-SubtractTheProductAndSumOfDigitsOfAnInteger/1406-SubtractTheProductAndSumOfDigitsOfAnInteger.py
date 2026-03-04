# Last updated: 04/03/2026, 13:34:36
class Solution(object):
    def subtractProductAndSum(self, n):
        #n = str()
        prod = 1
        sum = 0
        for i in list(str(n)):
            num = int(i)
            sum = sum + num
            prod = prod * num
        return prod - sum

        