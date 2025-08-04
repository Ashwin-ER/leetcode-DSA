class Solution(object):
    def isValid(self, s):
        stack = []
        d = {'(':')', '{':'}','[':']'}
        
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if stack == [] or d[stack.pop()] != i:
                    return False
                  
        return True if stack == [] else False