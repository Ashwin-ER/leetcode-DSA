class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if nums[i] > 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(nums)//2):
            nums[2*i]=arr1[i]
            nums[2*i + 1] = arr2[i]
        return nums
        

                