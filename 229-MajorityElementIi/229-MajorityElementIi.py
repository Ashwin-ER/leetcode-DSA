# Last updated: 04/03/2026, 13:35:28
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        mpp = defaultdict(int)

        mini = n // 3 + 1

        for num in nums:
            mpp[num] += 1

            if mpp[num] == mini:
                result.append(num)

            if len(result) == 2:
                break

        return result
        
