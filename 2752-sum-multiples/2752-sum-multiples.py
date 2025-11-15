class Solution(object):
    def sumOfMultiples(self, n):
        sum_range = 0
        for i in range(1,n+1):
            if i%3==0 or i % 5 == 0 or i % 7 == 0:
                sum_range += i
        return sum_range

