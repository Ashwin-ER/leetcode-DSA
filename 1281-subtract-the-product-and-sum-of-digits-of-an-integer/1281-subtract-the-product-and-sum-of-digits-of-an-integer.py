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

        