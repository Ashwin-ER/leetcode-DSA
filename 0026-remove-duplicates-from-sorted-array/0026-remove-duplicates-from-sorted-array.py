class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        insert_pos = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_pos] = nums[i]
                insert_pos = insert_pos + 1
        return insert_pos
        