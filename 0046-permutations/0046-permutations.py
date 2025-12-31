class Solution(object):
    def permute(self, nums):
        n = len(nums)
        sol, ans = [], []

        def backtract():
            if n == len(sol):
                ans.append(sol[:])
                return 
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtract()
                    sol.pop()
        backtract()
        return ans
            
