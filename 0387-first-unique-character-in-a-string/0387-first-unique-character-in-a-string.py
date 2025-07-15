class Solution(object):
    def firstUniqChar(self, s):
        count = Counter(s)
        for index , letter in enumerate(s):
            if count[letter] == 1:
                return index
        return -1