class Solution(object):
    def merge(self, nums1, m, nums2, n):
        insert = len(nums1) -1
        p1 = m-1
        p2 = n-1

        while p1>=0 and p2>=0:
            n1 = nums1[p1]   
            n2 = nums2[p2]   
            if n1>n2:
                nums1[insert] = n1
                p1 = p1 - 1
            else:
                nums1[insert] = n2
                p2 = p2 -1 
            insert = insert -1
        while p2>=0:
            nums1[insert] = nums2[p2]
            p2 = p2-1
            insert = insert -1


