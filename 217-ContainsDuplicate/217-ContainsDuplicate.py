# Last updated: 04/03/2026, 13:35:32
class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True