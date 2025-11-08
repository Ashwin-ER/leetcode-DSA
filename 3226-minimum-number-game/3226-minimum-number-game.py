class Solution:
    def numberGame(self, nums):#5423 
        nums.sort()            #2345
        res = []          
        for i in range(0, len(nums), 2):
            res.append(nums[i+1])  #3  #5
            res.append(nums[i])    #2  #4
        return res
