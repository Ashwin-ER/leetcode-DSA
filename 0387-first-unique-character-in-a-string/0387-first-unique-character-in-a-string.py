class Solution(object):
    def firstUniqChar(self, s):
        #count = Counter(s)
        #for index , letter in enumerate(s):
        #    if count[letter] == 1:
        #        return index
        #return -1

        count = {}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        for index , letter in enumerate(s):
            if count[letter] == 1:
                return index
        return -1
