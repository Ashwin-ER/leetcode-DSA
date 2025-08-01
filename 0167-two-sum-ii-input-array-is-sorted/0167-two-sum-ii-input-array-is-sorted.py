class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        l = 0
        r = n-1

        while r>l:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1,r+1]
            elif summ < target:
                l = l+1
            else:
                r = r-1 