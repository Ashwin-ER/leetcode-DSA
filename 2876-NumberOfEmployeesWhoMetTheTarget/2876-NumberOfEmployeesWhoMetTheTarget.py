# Last updated: 04/03/2026, 13:34:28
class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count = 0
        for i in hours:
            if i >= target:
                count+=1
        return count
        