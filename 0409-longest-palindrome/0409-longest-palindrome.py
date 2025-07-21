class Solution(object):
    def longestPalindrome(self, s):
        count = defaultdict(int)
        res = 0

        for char in s:
            count[char] += 1 
            if count[char]%2==0:
                res = res + 2
                
        for cnt in count.values():
            if cnt % 2:
                res = res + 1
                break
        return res

        


        