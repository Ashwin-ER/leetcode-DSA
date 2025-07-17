class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [] 
        max_len = 0
        
        for char in s:
            if char in arr:
                index = arr.index(char)
                arr = arr[index + 1:]
            arr.append(char)
            max_len = max(max_len, len(arr))
        
        return max_len
                
        