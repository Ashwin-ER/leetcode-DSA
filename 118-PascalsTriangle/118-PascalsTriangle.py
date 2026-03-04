# Last updated: 04/03/2026, 13:35:51
class Solution(object):
    def generate(self, num):
        if num == 1:
            return [[1]]
        elif num == 2:
            return [[1],[1,1]]
        else:
            ans = [[1],[1,1]]
            a = [1]
            b = [1,1]
            for i in range(num-2):
                for j in range(1,len(b)):
                    a.append(b[j-1]+b[j])
                a.append(1)
                ans.append(a)
                b=a
                a=[1]
            return ans


        