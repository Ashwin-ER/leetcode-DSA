class Solution(object):
    def topKFrequent(self, nums, k):
        hash = {}

        for i in nums:
            if i not in hash: 
                hash[i] = 1
            else:
                hash[i] += 1
        
        inverted = {}
        for key, value in hash.items():
            if value not in inverted:
                inverted[value] = [key]
            else:
                inverted[value].append(key)
        res = []
        for value in sorted(inverted.keys(), reverse = True):
            for num in inverted[value]:
                res.append(num)
                if len(res)==k:
                    return res
        return res

    
        