class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for i in nums:
            if i in count:
                count[i] = count[i] + 1
            else:
                count[i] = 1
        
        c = 0

        for i in nums:
            if count[i] > c:
                k = i
                c = count[i]
        return k
            


        