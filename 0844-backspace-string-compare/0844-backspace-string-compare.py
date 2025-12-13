class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l=[]
        m=[]
        for i in s:
            if i=='#':
                if l:
                    l.pop()
            else:
                l.append(i)
        for i in t:
            if i=='#':
                if m:
                    m.pop()
            else:
                m.append(i)
        return l==m