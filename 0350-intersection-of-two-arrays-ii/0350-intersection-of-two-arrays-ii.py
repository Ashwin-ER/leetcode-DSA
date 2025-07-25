class Solution(object):
    def intersect(self, nums1, nums2):
        counts = {}
        res = []
        
        for num in nums1:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        for num in nums2:
            if num in counts and counts[num]>0:
                res.append(num)
                counts[num] -= 1
        return res



                    
