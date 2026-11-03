# Last updated: 04/11/2026, 00:29:21
1class Solution(object):
2    def isValid(self, s):
3        stack = []
4        d = {'(':')', '{':'}','[':']'}
5        
6        for i in s:
7            if i in d:
8                stack.append(i)
9            else:
10                if stack == [] or d[stack.pop()] != i:
11                    return False
12                  
13        return True if stack == [] else False