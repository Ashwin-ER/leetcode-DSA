class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = []
        stack2 = []

        for i in s:
            if i=='#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        
        for i in t:
            if i=="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        
        return stack1 ==stack2

        